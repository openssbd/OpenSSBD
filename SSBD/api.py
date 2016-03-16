# SSBD/api.py
#from __future__ import unicode_literals
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
#import json as simplejson
#from django.core.serializers import json
#import simplejson as json
from tastypie.serializers import Serializer
#import ujson as json
#import cjson as json,from SSBD.SSBD2.models import *
from SSBD.SSBD2.bdmlweb_forms import *
from SSBD.BDML.models import *
from SSBD.SSBD2.models import *
#from SSBD.PDPML.models import *

#import ujson

class DatastreamSerializer(Serializer):
    def to_json(self, data, options=None):
        """
        Given some Python data, produces JSON output.
        """

        options = options or {}
        data = self.to_simple(data, options)
        return ujson.dumps(data)

    def from_json(self, content):
        """
        Given some JSON data, returns a Python dictionary of the decoded data.
        """
        return ujson.loads(content)


class metadataResource(ModelResource):
    class Meta:
        queryset = meta_data_model.objects.all()
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        resource_name = 'meta_data'
        include_resource_uri = False
        excludes = ['id', 'oldbdmlid', 'orf', 'gene']
        filtering = {
            'name' : ALL,
            'contributors' : ALL,
            'datatype' : ALL,
            'basedon' : ALL,
            'description' : ALL,
            'organization' : ALL,
            'department' : ALL,
            'laboratory' : ALL,
            'address' : ALL,
            'E_mail' : ALL,
            'localid' : ALL,
            'organism' : ALL,
        }     
        
class rootResource(ModelResource):
    meta_data = fields.ToOneField('SSBD.api.metadataResource', 'meta_data', full=True)
#    quant_data = fields.ToOneField('SSBD.api.quantdataResource', 'quant_data', full=True)
    class Meta:
        queryset = root_model.objects.all()
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        resource_name = 'data'
        include_resource_uri = True
        excludes = ['internal_bdml', 'internal_pdpml', 'internal_source', 'omero_datasetID', 'id', 'orf', 'oldbdmlid']
        filtering = {
            'bdmlUUID' : ['icontains', 'exact'],
            'meta_data' : ALL_WITH_RELATIONS,
            'localid' : ALL,
        }     
    def get_object_list(self, request):
        return super(rootResource, self).get_object_list(request).filter(status='available')  
        
class BDMLbdmlResource(ModelResource):
    class Meta:
        queryset = bdml_model.objects.all()
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        resource_name = 'bdml'
        include_resource_uri = False
#        fields = ['bdmlID', 'title']
        filtering = {
            'bdml_ID'   : ['icontains', 'exact'],
            'title'     : ALL_WITH_RELATIONS,
            'id'    : ALL,
            }

class BDMLInfoResource(ModelResource):
#    bdml = fields.ForeignKey(BDMLbdmlResource, 'bdml')
#    bdml = fields.ToOneField('SSBD.api.BDMLbdmlResource', 'bdml')

    class Meta:
        queryset = Info_model.objects.all()
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        resource_name = 'info'
        include_resource_uri = False
#        fields = ['bdml', 'title', 'bdmlID',]
        filtering = {
            'bdml' : ALL,
            'title' : ALL,
            'bdmlID' : ALL,
        }
#        serializer = DatastreamSerializer(formats=['json', 'xml', 'html', 'plist'])

class BDMLSummaryResource(ModelResource):
#    bdml = fields.ForeignKey(BDMLbdmlResource, 'bdml')
    bdml = fields.ToOneField('SSBD.api.BDMLbdmlResource', 'bdml', full=True)
    class Meta:
        queryset = Summary_model.objects.all()
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        resource_name = 'summary'
        include_resource_uri = False
#        fields = ['bdml', 'info']
#        fields = ['bdml', 'description', 'contributors', 'organism', 'identifier', 'datatype', 'basedon', 'title', 'bdmlID',]
        excludes = ['id']
        filtering = {
            'bdml' : ALL_WITH_RELATIONS,
            'description' : ALL,
            'contributors' : ALL,
            'organism' : ALL,
            'identifier' : ALL,
            'datatype' : ALL,
            'basedon' : ALL,
#            'bdml_ID' : ['icontains', 'exact'],
#            'bdmlrebdmlresource.bdmlID' : ('icontains','exact')
        }


class BDMLContactResource(ModelResource):
    bdml = fields.ToOneField('SSBD.api.BDMLbdmlResource', 'bdml', full=True)
    class Meta:
        queryset = Contact_model.objects.all()
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        resource_name = 'contact'
        include_resource_uri = False
        filtering = {
            'bdml' : ALL_WITH_RELATIONS,
            'name' : ALL,
            'organization' : ALL,
            'laboratory' : ALL,
            'department' : ALL,
            'address' : ALL,
        }
        
class coordsXYZResource(ModelResource):
    bdml = fields.ToOneField('SSBD.api.BDMLbdmlResource', 'bdml', full=True)
    class Meta:
        queryset = Coordinates_model.objects.all()
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        resource_name = 'coordsXYZ'
#        excludes = ['id' ]
        include_resource_uri = False
#max_limit - returns everything
        max_limit=100;
        fields = ['info', 'bdml', 'entity_id', 'entitytype', 'x', 'y', 'z', 'radius', 't']
        filtering = {
            'bdml' : ALL_WITH_RELATIONS,
#            'bdmlID' : ALL,
            'entitytype' : ALL,
#            'entity' : ALL,
#            'z' : ALL,
            't' : ALL,
#            'entity' : ALL_WITH_RELATIONS,
#usage: t__lt=5; t__range=80,82;
        }
#        serializer = DatastreamSerializer(formats=['json', 'xml', 'html', 'plist'])
#    def dehydrate(self, bundle):
#        bundle.data['entity'] = bundle.obj.entity_id
#        bundle.data['info'] = bundle.obj.bdmlID
#        del bundle.data['bdml']
#        del bundle.data['entity']
#        return bundle

class ScaleUnitResource(ModelResource):
    bdml = fields.ToOneField('SSBD.api.BDMLbdmlResource', 'bdml', full=True)
#    bdml = fields.ForeignKey(BDMLInfoResource, 'bdml')
    class Meta:
        queryset = ScaleUnit_model.objects.all()
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        resource_name = 'scale'
        include_resource_uri = False
        excludes = ['id', 'bdml', ]
        filtering = {
            'bdml' : ALL_WITH_RELATIONS,
            'tUnit' : ALL,
            'xyzUnit' : ALL,
            }


## The rest of this file are not implemented.

class componentResource(ModelResource):
    bdml = fields.ForeignKey(BDMLInfoResource, 'bdml')
#    measurement = fields.ToManyField('SSBD.api.measurementResource', 'measurement', full=True, null=True)
    class Meta:
        queryset = Component_model.objects.all()
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        resource_name = 'component'
        include_resource_uri = False
        filtering = {
            'name' : ALL,
            'componentid' : ALL,
            'bdml' : ALL,
        }

class measurementResource(ModelResource):
    bdml = fields.ForeignKey(BDMLInfoResource, 'bdml')
    component = fields.ForeignKey(componentResource, 'component', full=True, null=True)
    class Meta:
        queryset = Measurement_model.objects.all()
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        resource_name = 'measurement'
        include_resource_uri = False
#        fields = ['bdml', 'targetRef', 'value', 'component', 'measurementlist']
        filtering = {
            'bdml': ALL,
            'measurement_id' : ALL,
            'component_id' : ALL,
            'objectRef' : ALL,
            # component fields
            'component' : ALL_WITH_RELATIONS,
        }

class entityResource(ModelResource):
#    bdml = fields.ForeignKey(BDMLInfoResource, 'bdml')
    measurement = fields.ForeignKey(measurementResource, 'measurement', full=True)
    class Meta:
        queryset = Entity_model.objects.all()
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        resource_name = 'entity'
        include_resource_uri = False
#        fields = ['title', 'bdml', 'entitytype', 'x', 'y', 'z', 't', 'value', 'radius']
#        fields = ['title', 'bdml', 'entitytype',]
        filtering = {
            'bdml' : ALL,
            'title' : ALL,
            'entitytype' : ALL,
            'objectRef' : ALL,
            'measurement' : ALL_WITH_RELATIONS,
#            't' : ALL_WITH_RELATIONS,
        }


class coordinatesResource(ModelResource):
    bdml = fields.ForeignKey(BDMLInfoResource, 'bdml')
    entity = fields.ForeignKey(entityResource, 'entity', full=True)
    class Meta:
        queryset = Coordinates_model.objects.all()
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        resource_name = 'coordinates'
        include_resource_uri = False
#        fields = ['title', 'bdml', 'entity_id', 'entitytype', 'organism', 'identifier', 'x', 'y', 'z', 't', 'value', 'radius']
        fields = ['title', 'bdml', 'bdmlID', 'entity_id', 'entitytype', 'x', 'y', 'z', 't', 'value', 'radius']
        filtering = {
            'bdml' : ALL,
            'entitytype' : ALL,
            'z' : ALL,
            't' : ALL_WITH_RELATIONS,
            'entity' : ALL_WITH_RELATIONS,
#usage: t__lt=5; t__range=80,82;
        }



class compstatsResource(ModelResource):
#    comp = fields.ForeignKey(componentResource, 'comp')
    class Meta:
        queryset = compstats_model.objects.all()
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        resource_name = 'compstats'
#        excludes = ['id', 'bdml']
        include_resource_uri = False
        fields = ['bdml_id', 'comp', 'max_x', 'min_x', 'avg_x','max_y', 'min_y', 'avg_y', 'max_z', 'min_z', 'avg_z', 'max_t', 't', 'tp', 'componentName']
        filtering = {
# ToDo: as all other api uses bdml instead of bdml_id, it needs some form of coherency. Best to refactor it with SSBD2
            'bdml_id' : ALL,
#            'componentName' : ALL,
#            'comp' : ALL,
        }

class statsResource(ModelResource):
    bdml = fields.ForeignKey(BDMLInfoResource, 'bdml')
    class Meta:
        queryset = stats_model.objects.all()
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        resource_name = 'stats'
#        excludes = ['id', 'bdml']
        include_resource_uri = False
        fields = ['bdml', 'max_x', 'min_x', 'avg_x','max_y', 'min_y', 'avg_y', 'max_z', 'min_z', 'avg_z', 'max_t', 'min_t', 'min_tp', 'max_tp']
        filtering = {
            'bdml' : ALL,
            'max_t' : ALL,
            'min_t' : ALL,
        }




class VectorSerializer(Serializer):
    def to_json(self, data, options=None):
        """
        Given some Python data, produces JSON output.
        """
#        vector = []
#        for i in data:

        print "data: %s" % data

        options = options or {}
        data = self.to_simple(data, options)
        return ujson.dumps(data)

    def from_json(self, content):
        """
        Given some JSON data, returns a Python dictionary of the decoded data.
        """
        return ujson.loads(content)

class vectorsResource(ModelResource):
    bdml = fields.ForeignKey(BDMLInfoResource, 'bdml')
#    entity = fields.ForeignKey(entityResource, 'entity', full=False)
    class Meta:
        queryset = Coordinates_model.objects.all()
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        resource_name = 'vectors'
        excludes = ['id', 'bdml', ]
        include_resource_uri = False
        serializer = VectorSerializer(formats=['json', 'xml', 'html', 'plist'])
#max_limit - returns everything
        max_limit=None
        fields = ['entity', 'x', 'y', 'z', 't']
        filtering = {
            'bdml' : ALL,
            'entitytype' : ALL,
            'entity' : ALL,
            'z' : ALL,
            't' : ALL,
#            'entity' : ALL_WITH_RELATIONS,
#usage: t__lt=5; t__range=80,82;
        }
    def dehydrate(self, bundle):
#        print "bundle: %s " % bundle
        bundle.data['e'] = bundle.obj.entity_id
        del bundle.data['bdml']
#        del bundle.data['entity']
        return bundle

    def alter_list_data_to_serialize(self, request, data):
#        print "alter list data: %s" % data
        return data


class WEBPathResource(ModelResource):
#    bdmlmodel = fields.ToManyField('SSBD.api.bdmlResource', 'bdml_ID', related_name='bdmlID', null=True, blank=True, full=True)
    class Meta:
        queryset = Path_model.objects.all()
#        queryset = Path_model.objects.filter(path__bdmlID = bdmlResource.bdmlID)
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        resource_name = 'path'
        include_resource_uri = False
#        fields = ['image', 'bdmlID', 'bdml']
        fields = ['image', 'bdmlID', 'bdml_id']
        filtering = {
            'bdmlID' : ALL,
            'bdml_id' : ALL,
        }
class bdmlResource(ModelResource):
    webpath = fields.ToOneField('SSBD.api.WEBPathResource', 'bdmlID', related_name='bdml_ID', null=True, blank=True, full=True)
    class Meta:
        queryset = bdml_model.objects.all()
#        queryset = bdml.objects.filter(path__bdmlID = BDML.bdml_models.bdml_ID)
        print queryset.query
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        resource_name = 'bdml'
        include_resource_uri = False
        fields = ['id', 'title', 'bdml_ID',]
        filtering = {
            'bdml_ID' : ALL,
            'id' : ALL,
        }
        
class BDMLdocResource(ModelResource):
    class Meta:
        queryset = bdmlDocument_model.objects.all()
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        resource_name = 'bdmldoc'
        include_resource_uri = False
