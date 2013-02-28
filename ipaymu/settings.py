from django.conf import settings

# iPaymu API KEY
IPAYMU_APIKEY = getattr(settings, 'IPAYMU_APIKEY', None)

# Urls
IPAYMU_RETURN_URL = getattr(settings, 'IPAYMU_RETURN_URL', '/ipaymu/success/')
IPAYMU_CANCEL_URL = getattr(settings, 'IPAYMU_CANCEL_URL', '/ipaymu/canceled/')

# Return format (json/xml)
IPAYMU_RETURN_FORMAT = getattr(settings, 'IPAYMU_RETURN_FORMAT', 'json')

# Paypal Integration
IPAYMU_PAYPAL_EMAIL = getattr(settings, 'IPAYMU_PAYPAL_EMAIL', None)

# Transaction type
IPAYMU_ACTION = getattr(settings, 'IPAYMU_ACTION', 'payment')