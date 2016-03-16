from __future__ import unicode_literals
from django.conf.urls import patterns, url
from django.conf import settings
from django.views.generic import TemplateView
from SSBD.SSBD2.bdmlweb import DynamicPageView

urlpatterns = patterns('',
                       (r'^$', 'SSBD.SSBD2.bdmlweb.index'),
                       #
                       (r'^copyright/$', TemplateView.as_view(template_name="copyright.html")),
                       (r'^contact/$', TemplateView.as_view(template_name="contact.html")),
                       #
                       (r'^resources/$', DynamicPageView.as_view(template_name="resources.html")),
                       (r'^manuals/$', DynamicPageView.as_view(template_name="manuals.html")),
                       (r'^rdf/$', DynamicPageView.as_view(template_name="rdf.html")),
                       (r'^restfulapi/$', DynamicPageView.as_view(template_name="restfulapi.html")),
                       #
                       (r'^bdml/$', DynamicPageView.as_view(template_name="bdml/index.html")),
                       #(r'^bdml/(?P<filename>.+\.xsd)', 'SSBD.WEB.views.load_schema'),
                       (r'^bdml/(?P<filename>.+\.xsd)', 'SSBD.SSBD2.bdmlweb.load_schema'),
                       (r'^bdml/(?P<filename>.+\.html)$', lambda request, filename: DynamicPageView.as_view(template_name="bdml/"+filename)(request)),
                       #
                       (r'^pdpml/$', DynamicPageView.as_view(template_name="pdpml/index.html")),
                       (r'^pdpml/(?P<filename>.+\.xsd)$', 'SSBD.SSBD2.bdmlweb.load_schema'),
                       (r'^pdpml/(?P<filename>.+\.html)$', lambda request, filename: DynamicPageView.as_view(template_name="pdpml/"+filename)(request)),
                       #
                       (r'^omicsbdml/$', DynamicPageView.as_view(template_name="omicsbdml/index.html")),
                       (r'^omicsbdml/(?P<filename>.+\.xsd)$', 'SSBD.SSBD2.bdmlweb.load_schema'),
                       (r'^omicsbdml/(?P<filename>.+\.html)$', lambda request, filename: DynamicPageView.as_view(template_name="omicsbdml/"+filename)(request)),
                       #
                       (r'^BDML4DViewer/$', DynamicPageView.as_view(template_name="bdml4dviewer/index.html")),
                       (r'^BDML4DViewer/jar/(?P<filename>.+)$', 'SSBD.SSBD2.bdmlweb.download'),
                       (r'^BDML4DViewer/src/(?P<filename>.+)$', 'SSBD.SSBD2.bdmlweb.download'),
                       (r'^BDML4DViewer/(?P<template>.*)', lambda request, template: DynamicPageView.as_view(template_name="bdml4dviewer/"+template)(request)),
                       
                       (r'^phenochar/$', DynamicPageView.as_view(template_name="phenochar/index.html")),
                       (r'^phenochar/src/(?P<filename>.+)$', 'SSBD.SSBD2.bdmlweb.download'),
                       (r'^phenochar/(?P<template>.*)', lambda request, template: DynamicPageView.as_view(template_name="phenochar/"+template)(request)),
                       #
                       (r'^SSBD-OMERO\.insight/$', DynamicPageView.as_view(template_name="ssbd-omero/index.html")),
                       (r'^SSBD-OMERO\.insight/zip/(?P<filename>.*)$', 'SSBD.SSBD2.bdmlweb.download'),
                       #
                       (r'^publications/$', DynamicPageView.as_view(template_name="publications.html")),
                       (r'^download/$', DynamicPageView.as_view(template_name="download.html")),
                       (r'^software/$', DynamicPageView.as_view(template_name="download.html")),
                       #
                       (r'^search/(?P<uuid>.+)/', 'SSBD.SSBD2.bdmlweb.summary'),
                       (r'^history/(?P<id>.+)/', 'SSBD.SSBD2.bdmlweb.history'),
                       (r'^news/$', 'SSBD.SSBD2.bdmlweb.news'),
                       (r'^search/$', 'SSBD.SSBD2.bdmlweb.search'),
                       #
                       # viewer
                       (r'^view4d/(\d*)$', 'SSBD.SSBD2.bdmlweb.view4d'),
                       (r'^view4dline/(\d*)$', 'SSBD.SSBD2.bdmlweb.view4dline'),
                       #                       (r'^view4dt/(\d*)/t/(\d*)/$', 'SSBD.SSBD2.bdmlweb.view4dt'),
#                       (r'^view4dr/(\d*)/t/(\d*)/(\d*)/$', 'SSBD.SSBD2.bdmlweb.view4dr'),
                       # schema, manual, tools
                       (r'^doc/(?P<filename>.+)$', 'SSBD.SSBD2.bdmlweb.download_manual'),
                       # download XML and md5 data
                       (r'^data/source/(?P<projectname>.+)/(?P<filename>.+)/$', 'SSBD.SSBD2.bdmlweb.download_image'),
                       (r'^data/source/(?P<projectname>.+)/(?P<filename>.+)$', 'SSBD.SSBD2.bdmlweb.download_image'),
                       (r'^data/bdml/(?P<projectname>.+)/(?P<filename>.+)$', 'SSBD.SSBD2.bdmlweb.download_bdml'),
                       (r'^data/pdpml/(?P<filename>.+)$', 'SSBD.SSBD2.bdmlweb.download_pdpml'),
                       (r'^(?P<dirname>data.*)/$', 'SSBD.SSBD2.bdmlweb.list_dir'),
#                       (r'^qdb_data/(\d*)/$', 'SSBD.BDML.views.qdb_data'),
#                       (r'^vertices/(\d*)/t/(\d*)/etype/([a-z]+)/$', 'SSBD.BDML.views.vertices'),
#                       (r'^univertices/(\d*)/t/(\d*)/etype/([a-z]+)/$', 'SSBD.BDML.views.univertices'),
#                       (r'^vertices_avg/(\d*)/t/(\d*)/$', 'SSBD.BDML.views.vertices_avg'),
#                       (r'^vertices/(\d*)/t/(\d*)/(\d*)/etype/([a-z]+)/$', 'SSBD.BDML.views.vertices_range'),
)

if not settings.SSBD_SERVER:
    urlpatterns += patterns('',
#                            (r'^read_file/(?P<filename>.+)/$', 'SSBD.BDML.views.read_file'),
#                            (r'^read_file_nodata/(?P<filename>.+)/$', 'SSBD.BDML.views.read_file_nodata'),
#                            (r'^readMultipartFile/bdml/(?P<bdmlid>\d*)/(?P<filename>[-a-zA-Z0-9_.-\/]+)/$', 'SSBD.BDML.views.readMultipartFile'),
                            )
