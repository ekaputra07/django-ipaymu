from .settings import *


class IpaymuParamsBuilder(object):

    valid = False
    request = None

    def __init__(self, request):
        """
        Get Ipaymu request params from current request object (POST).
        """
        self.request = request

    def _build_params(self):
        """ 
        'key'      => 'api_key_merchant'
        'action'   => 'payment'
        'product'  => 'Nama Produk'
        'price'    => '101000'
        'quantity' => 1
        'comments' => 'Keterangan Produk'
        'ureturn'  => 'http://websiteanda.com/return.php',
        'unotify'  => 'http://websiteanda.com/notify.php',
        'ucancel'  => 'http://websiteanda.com/cancel.php',

        'invoice_number' => uniqid('INV-')
        'paypal_email'   => 'email_paypal_merchant'
        'paypal_price'   => 1
 
        'format'   => 'json'
        """
        pass

    def is_valid(self):
        return self.valid
        