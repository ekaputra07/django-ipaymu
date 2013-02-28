from django.core.urlresolvers import reverse
import settings

from forms import IpaymuForm


class InvalidIpaymuParams(Exception):
    pass


class IpaymuParamsBuilder(object):

    data = None
    raw_params = None
    cleaned_params = None
    errors = None

    def __init__(self, post_data):
        """
        Get Ipaymu request params from current request object (POST).
        """
        self.data = post_data
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

            # These parameters can be overrided via form
            'key': self.data.get('key') or settings.IPAYMU_APIKEY,
            'action': self.data.get('action') or settings.IPAYMU_ACTION,
            'ureturn': self.data.get('ureturn') or settings.IPAYMU_RETURN_URL,
            'ucancel': self.data.get('ucancel') or settings.IPAYMU_CANCEL_URL,
            'format': self.data.get('format') or settings.IPAYMU_RETURN_FORMAT,

            'paypal_email': self.data.get('paypal_email') or settings.IPAYMU_PAYPAL_EMAIL,
            'invoice_number': self.data.get('invoice_number', 'n/a'),
            'paypal_price': self.data.get('paypal_price'),

            'unotify': reverse('ipaymu_notify_url'),
        }
        return

    def is_valid(self):

        params = IpaymuForm(self.raw_params)

        if params.is_valid():
            self.cleaned_params = params.cleaned_data
            return True

        self.errors = params.errors
        return False

    def get_params(self):
        """ Validate and return Ipaymu params"""
        return self.params
        