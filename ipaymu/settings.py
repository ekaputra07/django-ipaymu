from django.conf import settings

# iPaymu API KEY
IPAYMU_APIKEY = 'need-your-ipaymu-api-key'

if hasattr(settings, 'IPAYMU_APIKEY'):
    IPAYMU_APIKEY = settings.IPAYMU_APIKEY

    