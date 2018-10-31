import requests
from requests.exceptions import Timeout, ConnectionError

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
import json

from ipaymu import settings
from ipaymu.utils import IpaymuParamsBuilder, execute_callback, save_session, verify_session


def process(request):
    """
    Process transaction request.
    """

    if request.method == 'POST':
        params = IpaymuParamsBuilder(request)

        if params.is_valid():

            # In case of connection/request error
            try:
                req = requests.post(settings.IPAYMU_REQUEST_URL, data=params.cleaned_params)
            except Timeout:
                return HttpResponse('Request timeout!.')
            except ConnectionError:
                return HttpResponse('Connection Error!.')

            # In case of empty response/Json Encode error
            try:
                resp_json = req.json()
            except:
                return HttpResponse('Empty response received!.')

            payment_url = resp_json.get('url')
            if payment_url:
                # Save session ID
                save_session(resp_json.get('sessionID'))
                # Execute callback when sessionID received.
                execute_callback('session_received', request, resp_json.get('sessionID'))
                return HttpResponseRedirect(payment_url)

            return HttpResponse(req.text)

        return HttpResponse(json.dumps(params.errors))
        
    return HttpResponse('Invalid request.')


@csrf_exempt
def notify(request):
    """
    This view point will be called by the iPaymu server on the background to notify
    the transaction has been success.
    """
    if request.method == 'POST':
        # Excecute callback if session ID verified.
        # Since we did't disable CSRF protection for this view.
        if(verify_session(request.POST.get('sid'))):
            execute_callback('notification_received', request, dict(request.POST))
    # Just return an empty response to avoid No Response error
    return HttpResponse('')


def return_page(request):
    """ Return page for Ipaymu transaction"""
    return render_to_response('ipaymu/return.html', context_instance=RequestContext(request))


def cancel_page(request):
    """ Cancel page for Ipaymu transaction"""
    return render_to_response('ipaymu/cancel.html', context_instance=RequestContext(request))


def test_page(request):
    """
    This page will contains some of common usages of Ipaymu,
    such as Donation form, Product checkout.
    """
    return render_to_response('ipaymu/test.html', context_instance=RequestContext(request))