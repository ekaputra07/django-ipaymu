from django.core.urlresolvers import reverse
from django.contrib.sites.shortcuts import get_current_site
from importlib import import_module

from ipaymu import settings
from ipaymu.forms import IpaymuForm
from ipaymu.models import IpaymuSessionID

class IpaymuCallbackError(Exception):
    pass

class IpaymuParamsBuilder(object):

    data = None
    raw_params = None
    cleaned_params = None
    errors = None
    request = None

    def __init__(self, request):
        """
        Get Ipaymu request params from current request object (POST).
        """
        self.request = request
        self.data = request.POST
        self._build_params()

    def _build_params(self):
        """
        Ipaymu parameters builder.
        Build params based on ipaymu requirements:
        https://ipaymu.com/cara-integrasi-webstore-tingkat-lanjut/

        ==Should be provided via form submit--------
        'product'  => 'Nama Produk'
        'price'    => '101000'
        'quantity' => 1
        'comments' => 'Keterangan Produk'

        ==Can be provided via Form submit or use default settings value
        'key'      => 'api_key_merchant'
        'action'   => 'payment',
        'ureturn'  => '/ipaymu/success/',
        'ucancel'  => '/ipaymu/canceled/',

        'invoice_number' => uniqid('INV-')
        'paypal_email'   => 'email_paypal_merchant'
        'paypal_price'   => 1

        'format'   => 'json'

        ---------- Django Ipaymu notification point ------------
        'unotify'  => '/ipaymu/notify/',
        """

        self.raw_params = {
            # These parameters must provided via form
            'product': self.data.get('product', 'n/a'),
            'price': self.data.get('price', 0),
            'quantity': self.data.get('quantity', 0),
            'comments': self.data.get('comments', ''),

            # These parameters can be overrided via form or settings
            'key': self.data.get('key') or settings.IPAYMU_APIKEY,
            'action': self.data.get('action') or settings.IPAYMU_ACTION,
            'format': self.data.get('format') or settings.IPAYMU_RETURN_FORMAT,
            'paypal_email': self.data.get('paypal_email') or settings.IPAYMU_PAYPAL_EMAIL,
            'invoice_number': self.data.get('invoice_number', 'n/a'),
            'paypal_price': self.data.get('paypal_price'),

            'ureturn': self.data.get('ureturn') or settings.IPAYMU_RETURN_URL or ('%s%s%s' % (settings.SITE_PROTOCOL,
                                    get_current_site(self.request).domain,
                                    reverse('ipaymu_return_url'))),

            'ucancel': self.data.get('ucancel') or settings.IPAYMU_CANCEL_URL or ('%s%s%s' % (settings.SITE_PROTOCOL,
                                    get_current_site(self.request).domain,
                                    reverse('ipaymu_cancel_url'))),

            'unotify': '%s%s%s' % (settings.SITE_PROTOCOL,
                                    get_current_site(self.request).domain,
                                    reverse('ipaymu_notify_url')),
        }
        return

    def is_valid(self):
        """ Check if data posted is valid"""
        params = IpaymuForm(self.raw_params)

        if params.is_valid():
            self.cleaned_params = params.cleaned_data
            return True

        self.errors = params.errors
        return False
        

def execute_callback(name, *args):
    """ Execute provided callback """

    callbacks = settings.IPAYMU_CALLBACKS
    callback_string = callbacks.get(name)

    if callback_string and isinstance(callback_string, basestring):
        # Fail silently when callback error
        # Just notify via log console.

        # Split callback namespace to module and its function
        ns = callback_string.split('.')
        callback_func = ns[-1]
        callback_module_str = '.'.join(ns[:-1])

        try:
            callback_module = import_module(callback_module_str)
            getattr(callback_module, callback_func)(*args)
        except ImportError as e:
            raise IpaymuCallbackError('Could not import Ipaymu callback module \'%s\'' % (callback_module_str))
        except AttributeError as e:
            raise IpaymuCallbackError('\'%s\' has no attribute \'%s\'' % (callback_module_str, callback_func))
    return


def save_session(sessid):
    """ Save received session ID to database """

    session = IpaymuSessionID(sessid=sessid)
    session.save()
    return


def verify_session(sessid):
    """ Verify session ID that come from Ipaymu notification request """
    
    try:
        session = IpaymuSessionID.objects.get(sessid=sessid)
        session.verified=True
        session.save()
    except IpaymuSessionID.DoesNotExist:
        return False
    return True