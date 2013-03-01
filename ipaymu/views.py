import requests
from requests.exceptions import Timeout, ConnectionError

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson

import settings
from utils import IpaymuParamsBuilder


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
                # on_session_receieved callback must go here, before redirect to Ipaymu
                return HttpResponseRedirect(payment_url)
            return HttpResponse(req.text)

        return HttpResponse(simplejson.dumps(params.errors))
        
    return HttpResponse('Invalid request.')


def notify(request):
    """
    This view point will be called by the iPaymu server on the background to notify
    the transaction has been success.
    """
    pass

def test_page(request):
    """
    This page will contains some of common usages of Ipaymu,
    such as Donation form, Product checkout.
    """
    return render_to_response('ipaymu/test.html', locals(), context_instance=RequestContext(request))