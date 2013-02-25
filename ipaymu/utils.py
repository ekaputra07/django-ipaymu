from django.core.urlresolvers import reverse
import settings

class InvalidIpaymuParams(Exception):
    pass


class IpaymuParamsBuilder(object):

    valid = False
    data = None
    params = {}

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

        -------- shoulf be provided via form submit--------
        'product'  => 'Nama Produk'
        'price'    => '101000'
        'quantity' => 1
        'comments' => 'Keterangan Produk'

        ---------- Can be provided via Form submit or use default settings value ------

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

        self.params = {
            'key': self.data.get('key', settings.IPAYMU_APIKEY),
            'action': self.data.get('action', settings.IPAYMU_ACTION),
            'unotify': reverse('notify_url'),
            'ureturn': self.data.get('ureturn', settings.IPAYMU_RETURN_URL),
            'ucancel': self.data.get('ucancel', settings.IPAYMU_CANCEL_URL),
            'format': self.data.get('format', settings.IPAYMU_RETURN_FORMAT),
        }

        if self.data.get('accept_paypal'):
            self.params.update({
                'invoice_number': self.data.get('invoice_number', None),
                'paypal_email': self.data.get('paypal_email', settings.IPAYMU_PAYPAL_EMAIL),
                'paypal_price': self.data.get('paypal_price'),
            })

    def _validate_params(self):
        """
        Validate params to ensure 
        """
        raise InvalidIpaymuParams('Field tidak valid.')

    def get_params(self):
        """ Validate and return Ipaymu params"""
        self._validate_params()
        return self.params
        