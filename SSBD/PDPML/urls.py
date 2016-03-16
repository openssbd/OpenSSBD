from __future__ import unicode_literals
from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
                       )

if not settings.SSBD_SERVER:
    urlpatterns += patterns('',
                            (r'^read_pdpml/(?P<filename>[a-zA-Z0-9_.-]+)/$', 'SSBD.PDPML.views.read_pdpml'),
                            )
