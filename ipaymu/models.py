from django.db import models
from django.utils.translation import ugettext_lazy as _

class IpaymuSessionID(models.Model):
    """
    This model to store Ipaymu session ID for each transaction.

    Will be used for verification layer when notification occurs.
    Session ID will be recorded during the process, and will be verified
    when notification request come.
    If session exists, notification is valid, otherwise its invalid.

    This verification needed since notify URL is opened to public without CSRF
    protection, to avoid mallicious request atempt. 
    """
    sessid = models.TextField(_('Session ID'), db_index=True)

    class Meta:
        db_table = 'ipaymu_sessid'
