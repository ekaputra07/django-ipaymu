from django.conf import settings

# Site protocol (http:// or https://)
SITE_PROTOCOL = getattr(settings, 'SITE_PROTOCOL', 'http://')

# Request url
IPAYMU_REQUEST_URL = getattr(settings, 'IPAYMU_REQUEST_URL', 'https://my.ipaymu.com/payment.htm')

# iPaymu API KEY
IPAYMU_APIKEY = getattr(settings, 'IPAYMU_APIKEY', None)

# Urls
IPAYMU_RETURN_URL = getattr(settings, 'IPAYMU_RETURN_URL', None)
IPAYMU_CANCEL_URL = getattr(settings, 'IPAYMU_CANCEL_URL', None)

# Return format (json/xml)
IPAYMU_RETURN_FORMAT = getattr(settings, 'IPAYMU_RETURN_FORMAT', 'json')

# Paypal Integration
IPAYMU_PAYPAL_EMAIL = getattr(settings, 'IPAYMU_PAYPAL_EMAIL', None)

# Transaction type
IPAYMU_ACTION = getattr(settings, 'IPAYMU_ACTION', 'payment')

# Ipaymu Callback
IPAYMU_CALLBACKS = getattr(settings, 'IPAYMU_CALLBACKS',{
            'session_received': None,
            'notification_received': None,
        }
    )