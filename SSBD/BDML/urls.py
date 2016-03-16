from __future__ import unicode_literals
from django.conf.urls import patterns
from django.conf import settings

urlpatterns = patterns('',
                       (r'^qdb_data/(\d*)/$', 'SSBD.BDML.views.qdb_data'),
                       (r'^vertices/(\d*)/t/(\d*)/etype/([a-z]+)/$', 'SSBD.BDML.views.vertices'),
                       (r'^univertices/(\d*)/t/(\d*)/etype/([a-z]+)/$', 'SSBD.BDML.views.univertices'),
                       (r'^univerticestp/(\d*)/tp/(\d*)/etype/([a-z]+)/$', 'SSBD.BDML.views.univerticestp'),
                       (r'^vertices_avg/(\d*)/t/(\d*)/$', 'SSBD.BDML.views.vertices_avg'),
                       (r'^vertices/(\d*)/t/(\d*)/(\d*)/etype/([a-z]+)/$', 'SSBD.BDML.views.vertices_range'),
)

if not settings.SSBD_SERVER:
	urlpatterns += patterns('',
                            (r'^read_file/(?P<filename>.+)/$', 'SSBD.BDML.views.read_file'),
                            )
