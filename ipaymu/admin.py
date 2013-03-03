from django.contrib import admin

from ipaymu.models import IpaymuSessionID

class IpaymuSessionIDAdmin(admin.ModelAdmin):
    list_display = ['sessid', 'verified', 'created', 'updated']

admin.site.register(IpaymuSessionID, IpaymuSessionIDAdmin)