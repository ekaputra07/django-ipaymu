from django.conf import settings

try:
    from django.conf.urls import patterns, include, url
except:
    # Support for Django < 1.4
    from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('ipaymu.views',
    url(r'^process/$', 'process', name='process_url'),
    url(r'^notify/$', 'notify', name='notify_url'),
    url(r'^success/$', 'success_page', name='success_page'),
    url(r'^canceled/$', 'cancel_page', name='cancel_page'),
)

# Ipaymu test page available only in Debug mode.
if settings.DEBUG:
    urlpatterns += patterns('ipaymu.views',
        url(r'^testpage/$', 'test_page', name='test_page'),
    )