from __future__ import unicode_literals

from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf.urls import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from api import BDMLInfoResource, \
                rootResource, \
                metadataResource, \
                coordsXYZResource, \
                ScaleUnitResource, \
                BDMLSummaryResource, \
                BDMLContactResource, \
                BDMLbdmlResource
#                entityResource, \
#                componentResource, \
#                measurementResource, \
#                coordinatesResource, \
#                compstatsResource, \
#                statsResource, \
#                vectorsResource, \
#                BDMLdocResource, \
#                WEBPathResource, \

v1_api = Api(api_name='v1')
v1_api.register(rootResource())
v1_api.register(metadataResource())
v1_api.register(BDMLInfoResource())
#v1_api.register(BDMLInfoResource2())
v1_api.register(BDMLbdmlResource())
v1_api.register(BDMLSummaryResource())
v1_api.register(BDMLContactResource())
#v1_api.register(BDMLdocResource())
#v1_api.register(entityResource())
#v1_api.register(componentResource())
#v1_api.register(measurementResource())
#v1_api.register(coordinatesResource())
#v1_api.register(BDMLdocResource())
#v1_api.register(WEBPathResource())
#v1_api.register(entityResource())
#v1_api.register(componentResource())
#v1_api.register(measurementResource())
#v1_api.register(coordinatesResource())
#v1_api.register(statsResource())
v1_api.register(coordsXYZResource())
#v1_api.register(vectorsResource())
v1_api.register(ScaleUnitResource())

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('SSBD.SSBD2.urls')),
    url(r'^SSBD/PDPML/', include('SSBD.PDPML.urls')),
    url(r'^SSBD/BDML/', include('SSBD.BDML.urls')),
    url(r'^SSBD/api/', include(v1_api.urls)),
)
