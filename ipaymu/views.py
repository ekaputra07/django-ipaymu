from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson

from .settings import *
from .utils import IpaymuParamsBuilder


def process(request):
    """
    Process transaction request.
    """

    if request.method == 'POST':
        params = IpaymuParamsBuilder(request.POST)

        if params.is_valid():
            return HttpResponse(str(params.cleaned_params))
        return HttpResponse(simplejson.dumps(params.errors))

    return HttpResponse('Invalid request.')


def notify(request):
    """
    This view point will be called by the iPaymu server on the background to notify
    the transaction has been success.
    """
    pass


def return_page(request):
    """
    Page that displayed when transaction success. 
    You mostly will say thank you here.
    """
    return render_to_response('ipaymu/success.html', context_instance=RequestContext(request))


def cancel_page(request):
    """
    Page that will displayed if Ipaymu payment canceled.
    """
    return render_to_response('ipaymu/cancel.html', context_instance=RequestContext(request))


def test_page(request):
    """
    This page will contains some of common usages of Ipaymu,
    such as Donation form, Product checkout.
    """
    return render_to_response('ipaymu/test.html', locals(), context_instance=RequestContext(request))