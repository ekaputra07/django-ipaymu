from django.conf.urls import patterns, include, url
from django.conf import settings


urlpatterns = patterns('ipaymu.views',
    url(r'^process/$', 'process_post', name='post_url'),
    url(r'^notify/$', 'notify', name='notify_url'),
    url(r'^success/$', 'success_page', name='success_page'),
    url(r'^canceled/$', 'cancel_page', name='cancel_page'),
)

# Ipaymu test page available only in Debug mode.
if settings.DEBUG:
    urlpatterns += patterns('ipaymu.views',
        url(r'^testpage/$', 'test_page', name='test_page'),
    )