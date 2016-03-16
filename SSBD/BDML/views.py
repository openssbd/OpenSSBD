# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.core import serializers
from django.db.models import Q, Max, Min, Avg

myDebug=False

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
import json 

from models import *

from xml.dom import minidom    # needed by generateDS
from xml.dom import Node       # needed by generateDS
import bdmllib    # generateDS generated bdml interface
bdmldir='/tmp/bdml/'

def univertices(request, bdmlid, time, etype):
    try:
#        verticeslist = unicoords_model.objects.filter(bdml=bdmlid, t=time, entitytype=etype).order_by("entity","id")
        verticeslist = unicoords_model.objects.filter(bdml=bdmlid, t=time, entitytype=etype).order_by("coords","id")
        data = process_vertices(verticeslist, etype)
    except:
        errortext = {"univertices" : "error: cannot retrieve vertices"} # cannot retrieve vertices
        data = json.dumps('json',errortext)
    if 'callback' in request.REQUEST:
    # a jsonp response!
        data = '%s(%s);' % (request.REQUEST['callback'], data)
        return HttpResponse(data, "text/javascript")
    else:
        return HttpResponse(data, mimetype='application/json')

def univerticestp(request, bdmlid, tp, etype):
    try:
#        verticeslist = unicoords_model.objects.filter(bdml=bdmlid, t=time, entitytype=etype).order_by("entity","id")
        verticeslist = unicoords_model.objects.filter(bdml=bdmlid, timept=tp, entitytype=etype).order_by("coords","id")
        data = process_vertices(verticeslist, etype)
    except:
        errortext = {"univertices" : "error: cannot retrieve vertices"} # cannot retrieve vertices
        data = json.dumps('json',errortext)
    if 'callback' in request.REQUEST:
    # a jsonp response!
        data = '%s(%s);' % (request.REQUEST['callback'], data)
        return HttpResponse(data, "text/javascript")
    else:
        return HttpResponse(data, mimetype='application/json')

def stats(request, bdmlid, time):
    try:
        print "vertices_avg"
        data = unicoords_model.objects.filter(bdml_id=bdmlid, t=time).aggregate(
                    avgx=Avg('x'),
                    avgy=Avg('y'),
                    avgz=Avg('z'),
                    xmax=Max('x'),
                    xmin=Min('x'),
                    ymax=Max('y'),
                    ymin=Min('y'),
                    zmax=Max('z'),
                    zmin=Min('z'),
                    )
    except:
        errortext = {"vertices_avg" : "error"} # cannot retrieve vertices
        data = json.dumps('json',errortext)
    if 'callback' in request.REQUEST:
    # a jsonp response!
        data = '%s(%s);' % (request.REQUEST['callback'], data)
        return HttpResponse(data, "text/javascript")
    else:
        return HttpResponse(data, mimetype='application/json')

def vertices(request, bdmlid, time, etype):
    try:
        verticeslist = Coordinates_model.objects.filter(bdml=bdmlid, t=time, entitytype=etype).order_by("entity","id")
        data = process_vertices(verticeslist, etype)
    except:
        errortext = {"vertices" : "error"} # cannot retrieve vertices
        data = json.dumps('json',errortext)
    if 'callback' in request.REQUEST:
    # a jsonp response!
        data = '%s(%s);' % (request.REQUEST['callback'], data)
        return HttpResponse(data, "text/javascript")
    else:
        return HttpResponse(data, mimetype='application/json')

def vertices_avg(request, bdmlid, time):
    try:
        print "vertices_avg"
        data = Coordinates_model.objects.filter(bdml_id=bdmlid, t=time).aggregate(
                    avgx=Avg('x'),
                    avgy=Avg('y'),
                    avgz=Avg('z'),
                    xmax=Max('x'),
                    xmin=Min('x'),
                    ymax=Max('y'),
                    ymin=Min('y'),
                    zmax=Max('z'),
                    zmin=Min('z'),
                    )

#        print "data: %s" % data
#        data = {'bdml_id': bdmlid, 'avgx' : avgx, 'avgy' : avgy, 'avgz' : avgz, 't' : time }
#               'tmin' : time_min,
#               'tmax' : time_max,
#               'min_t': minmax_t['time__min'],
#               'max_t': minmax_t['time__max'],
#               'cam_x': avgx*scale.xScale*scaleup,
#               'cam_y': avgy*scale.yScale*scaleup,
#               'cam_z': avgz*scale.zScale*scaleup,
#               'xmax' : xmax,
#               'ymax' : ymax,
#               'xmin' : xmin,
#               'ymin' : ymin,
#               'xscale': scale.xScale*scaleup,
#               'yscale': scale.yScale*scaleup,
#               'zscale': scale.zScale*scaleup,
#               'scaleup' : scaleup,
#               }
#        data = process_vertices(verticeslist, etype)
    except:
        print "error"
        errortext = {"vertices" : "error"} # cannot retrieve vertices
        data = json.dumps('json',errortext)
    if 'callback' in request.REQUEST:
    # a jsonp response!
        data = '%s(%s);' % (request.REQUEST['callback'], data)
        return HttpResponse(data, "text/javascript")
    else:
        return HttpResponse(json.dumps(data), mimetype='application/json')

def vertices_range(request, bdmlid, time_min, time_max, etype):
    try:
        verticeslist = Coordinates_model.objects.filter(bdml=bdmlid, t__gte=time_min, t__lte=time_max, entitytype=etype).order_by("entity","id")
        data = process_vertices(verticeslist, etype)
    except:
        errortext = {"vertices" : "error"} # cannot retrieve vertices
        data = json.dumps('json',errortext)
    if 'callback' in request.REQUEST:
    # a jsonp response!
        data = '%s(%s);' % (request.REQUEST['callback'], data)
        return HttpResponse(data, "text/javascript")
    else:
        return HttpResponse(data, mimetype='application/json')

def process_vertices(vlist, etype):
        debugPrint("starting")
        debugPrint("verticeslist %s" % vlist)
        if vlist.count() != 0:
            v =""
            for i in vlist:
                if etype == "sphere":
                    debugPrint("%s %s %s %s %s %s %s" % (i.entity_id, i.id, i.x, i.y, i.z, i.t, i.radius))
                    v+="%s %s %s %s %s %s %s " % (i.entity_id, i.id, i.x, i.y, i.z, i.t, i.radius)
                else:
                    debugPrint("%s %s %s %s %s %s" % (i.entity_id, i.id, i.x, i.y, i.z, i.t))
                    v+="%s %s %s %s %s %s " % (i.entity_id, i.id, i.x, i.y, i.z, i.t)
            debugPrint(v)
            varray = v.split()
#            debugPrint(varray)
#            vl = [float(j) for j in varray]
            vl = map(float, varray)
            debugPrint(vl)
            returnobject = {"vertices" : vl}
            data = json.dumps(returnobject)
        else:
            emptytext = {"vertices" : "error"} # no data
            data = json.dumps(emptytext)
        return data




# The decorator allows Django to roll back the transaction if the function raises an exception
@transaction.commit_on_success
def read_file(request, filename):
    """
    Reading in a BDML file and binding its content to bdml model and save that in the database
    except it will not save any information from Data tag
    :param request:
    :param filename:
    bdml_instance = bdml_api.parse('/tmp/wt-CDD0301160201.bdml')
    bdml_instance = bdml_api.parse('/tmp/split-wt-CDD0301160201.bdml')
    bdml_instance = bdml_api.parse('/tmp/bao-wild-type-embryo.bdml')
    check database and see whether the same document exists - check info.title, summary.contributors, info.version
    reading in bdml file using genereateDS
    """
    outdata = {}
    try:
        import os
        bdmlfile = os.path.join(bdmldir, filename)
        debugPrint("bdmlfile = %s" % bdmlfile)
        bdmlfile_instance = bdmllib.parse(bdmlfile)
        checkbdmlid = bdmlfile_instance.info.bdmlID
        debugPrint("BDML ID: %s" % checkbdmlid)
        dbInfo = Info_model.objects.filter(bdmlID=checkbdmlid)
        if len(dbInfo) != 0: # same contributors found in the existing database
                debugPrint("DB bdml ID %s" % dbInfo[0].bdmlID)
                debugPrint("The same BDML data exists in the database")
                debugPrint("This BDML file will not be read into the database")
                outdata = {
                    'error' : 'Same BDML data exists in the database',
                    'BDML ID' : checkbdmlid,
                }
        else:
            debugPrint("The BDML does not appear in this database")
            debugPrint("Reading the BDML data into the database")
            outdata = binding_bdml(bdmlfile_instance)
            #check to see whether there is any exception error, if there is, then raise exception.
            if outdata['error'] != 'none':
                raise Exception(outdata)
            debugPrint("finishing binding_bdml 2")
    except Exception as e:
        outdata = {
            'error': "Cannot save BDML in the database",
            'details': "%s" % e,
        }
    debugPrint(outdata)
    jsonlist = json.dumps(outdata)
    return HttpResponse(jsonlist, mimetype='application/javascript; charset=UTF-8')

@transaction.commit_on_success
def binding_bdml(bdml_instance):
    """
        Binding BDML_Document model into Django Object Orientated model
    :param bdml_instance:
        : param bdml_instance: bdml instance through bdml_api
    """
    outdata = {}
    debugPrint("start binding_bdml")
    try:
	debugPrint("title: %s" % bdml_instance.info.title)
        debugPrint("bdmlID: %s" % bdml_instance.info.bdmlID)
        new_bdml = bdml_model(
                title = bdml_instance.info.title,
                bdml_ID = bdml_instance.info.bdmlID,
        )
        print("saving bdml model")
        new_bdml.save()
        bdmlid = new_bdml
        print("bdml saved, bdmlid:%s" %bdmlid)

        #Mapping Info model
        new_info = Info_model(
            bdml = bdmlid,
            bdmlID = bdml_instance.info.bdmlID,
            title=bdml_instance.info.title,
            version=bdml_instance.info.version,
            release=bdml_instance.info.release,
            license=bdml_instance.info.license,
        )
        print("saving info")
        new_info.save()
        infoid = new_info
        print("info saved")
        print("info saved, infoid:%s" %infoid)

        #Mapping Summary model
        new_summary = Summary_model(
            bdml = bdmlid,
            description=bdml_instance.summary.description,
            organism=bdml_instance.summary.organism,
            datatype=bdml_instance.summary.datatype,
            identifier=bdml_instance.summary.identifier,
            basedon=bdml_instance.summary.basedon,
            contributors=bdml_instance.summary.contributors,
            citation=bdml_instance.summary.citation,
            PMID=bdml_instance.summary.PMID,
            dblink=bdml_instance.summary.dblink,
        )
        print("saving summary")
        new_summary.save()
        summaryid = new_summary
        print("summary saved")
        print("summary saved, summaryid:%s" %summaryid)

        #Mapping Contact model
        new_contact = Contact_model(
            bdml = bdmlid,
            name = bdml_instance.contact.name,
            E_mail=bdml_instance.contact.E_mail,
            phone=bdml_instance.contact.phone,
            URL=bdml_instance.contact.URL,
            organization=bdml_instance.contact.organization,
            department=bdml_instance.contact.department,
            laboratory=bdml_instance.contact.laboratory,
            address=bdml_instance.contact.address,
        )
        print("saving contacts")
        new_contact.save()
        contactid = new_contact
        print("contacts saved")
        print("contacts saved, contactid:%s" %contactid)

        #Mapping Methods model
        new_methods = Methods_model(
            bdml = bdmlid,
            summary=bdml_instance.methods.summary,
            source=bdml_instance.methods.source,
            pdpml=bdml_instance.methods.pdpml,
        )
        print("saving methods")
        new_methods.save()
        methodsid = new_methods
        print("methods saved")
        print("methods saved, methodsid:%s" %methodsid)

        #Above entities are independent of each others and they are not nested.
        #Below entities are nested and need to iterate before they can be saved accordingly

        #Mapping scaleUnit model
        new_scaleunit = ScaleUnit_model(
            bdml = bdmlid,
            xScale=bdml_instance.data.scaleUnit.xScale,
            yScale=bdml_instance.data.scaleUnit.yScale,
            zScale=bdml_instance.data.scaleUnit.zScale,
            tScale=bdml_instance.data.scaleUnit.tScale,
            xyzUnit=bdml_instance.data.scaleUnit.xyzUnit,
            tUnit=bdml_instance.data.scaleUnit.tUnit,
        )
        print("saving scaleunit")
        new_scaleunit.save()
        scaleunitid = new_scaleunit
        print("scaleunit saved, scaleunit:%s" %scaleunitid)

        #Mapping Data model
        new_data = Data_model(
            bdml = bdmlid,
            scaleUnit = scaleunitid,
        )
        print("saving data")
        new_data.save()
        dataid = new_data
        print("data %s saved" %dataid)

        #Mapping Object model
#        for i in bdml_instance.data.object:
#        while bdml_instance.get_data().get_object() != None:
        objectlist = bdml_instance.get_data().get_object()
        for i in objectlist:
                debugPrint("len objectlist %s" % len(objectlist))
                debugPrint("object i %s" %i)
                debugPrint("objectName: %s" % i.get_objectName())
                new_object = Object_model(
                    bdml = bdmlid,
                    objectName=i.get_objectName(),
                    data = dataid,
                )
                print("saving object")
                new_object.save()
                objectid = new_object
                print("object %s saved" %objectid)

        #Mapping Feature model
        debugPrint("starting processing feature")
        if bdml_instance.data.get_feature() != []:
            debugPrint("feature exists")
            featurelist = bdml_instance.get_data().get_feature()
            for ii in featurelist:
                debugPrint("len featurelist %s" % len(featurelist))
                debugPrint("feature ii %s" %ii)
                debugPrint("featureName: %s" % ii.get_featureName())
                debugPrint("featureScale: %s" % ii.get_featureScale())
                debugPrint("featureUnit: %s" % ii.get_featureUnit())
                new_feature = Feature_model(
                    bdml = bdmlid,
                    featureName=ii.get_featureName(),
                    featureScale=ii.get_featureScale(),
                    featureUnit=ii.get_featureUnit(),
                    data = dataid,
                )
                debugPrint("saving feature")
                new_feature.save()
                featureid = new_feature
                debugPrint("feature %s saved" %featureid)
        else:
            debugPrint("feature does not exist")

        #Mapping Component model
        debugPrint("starting to bind component")
        componentlist = bdml_instance.data.get_component()
        debugPrint("len(componentlist) = %s" % len(componentlist))
        if componentlist == []:
            debugPrint("no component!!")
        else:
            for j in componentlist:
                new_component = Component_model(
                    bdml = bdmlid,
                    componentID=j.get_componentID(),
                    componentName = j.get_componentName(),
                    time=float(j.get_time()),
                    data = dataid,
                )
                debugPrint("saving component")
                debugPrint("bdml=%s, dataid=%s, componentid=%s, time=%s, componentname=%s, float-time=%s" % (bdmlid, dataid, j.get_componentID(), j.get_time(), j.get_componentName(), float(j.get_time())))
                new_component.save()
                component_dbid = new_component
                debugPrint("component %s saved" %component_dbid)

        #Mapping PrevID model
                if j.get_prevID() != []:
                    debugPrint("prevID exists")
                    prevIDlist = j.get_prevID()
                    debugPrint("len(prevIDlist)=%s" % len(prevIDlist))
                    for jp in j.prevID:
                        debugPrint("prevID exists %s" % jp)
                        new_previdmodel = PrevID_model(
                            bdml = bdmlid,
                            component = component_dbid,
                            data = dataid,
                            prevID = jp,
                        )
                        debugPrint("saving prevID")
                        new_previdmodel.save()
                        previdmodelid = new_previdmodel
                        debugPrint("prevID %s saved" % previdmodelid)
                else:
                    debugPrint("no prevID")

            #Mapping GroupID model
                if j.get_groupID() != []:
                    debugPrint("groupID exists")
                    groupIDlist = j.get_groupID()
                    debugPrint("len(groupIDlist)=%s" % len(groupIDlist))
                    for jg in j.groupID:
                        debugPrint("groupID exists %s" % jg)
                        new_groupidmodel = GroupID_model(
                            bdml = bdmlid,
                            component = component_dbid,
                            data = dataid,
                            groupID = jg,
                        )
                        debugPrint("saving groupID")
                        new_groupidmodel.save()
                        groupidmodelid = new_groupidmodel
                        debugPrint("groupID %s saved" % groupidmodelid)

                else:
                    debugPrint("no groupID")
            #Mapping Measurement model
                for k in j.get_measurement():
                    new_measurement = Measurement_model(
                        bdml = bdmlid,
                        objectRef=k.get_objectRef(),
                        component = component_dbid,
                    )
                    debugPrint("saving measurement bdml %s, objectRef %s,  \
                      component %s" \
                      % (bdmlid, k.get_objectRef(), component_dbid))
                    new_measurement.save()
                    measurementid = new_measurement
                    debugPrint("measurement %s saved" %measurementid)


                #Mapping Line model to Entity model
                #checking if it is empty before proceed
                    if k.get_line() != None:
                        debugPrint("found line")
                        debugPrint("creating entity")
                        lines_coords = k.get_line().get_coords()
                        debugPrint("lines coords %s" % lines_coords)
                        # coordinates of lines; linecoords="coordindates of each line"
                        for linecoords in lines_coords:
                            entityid = create_entity(bdmlid, component_dbid, measurementid, 'line')
#                            debugPrint("line: bdmlid %s, entityid %s, linecoords %s, time %s " % (bdmlid, entityid, k.get_line().get_coords(), j.get_time() ))
                            debugPrint("line: bdmlid %s, entityid %s, linecoords %s, time %s " % (bdmlid, entityid, linecoords, j.get_time() ))
                            process_coordinates(bdmlid, entityid, linecoords, 'line', j.get_time(), None)
                            propertylist = k.get_line().get_property()
                            debugPrint("len(propertylist) %s" % len(propertylist))
                            if len(propertylist) != 0:
                                debugPrint("creating property")
#                               for l in propertylist:
#                                   create_property(bdmlid, entityid, l)
                                create_property(bdmlid, entityid, propertylist)
                            else:
                                debugPrint("no property")

#TODO replicate sphere to circle
                #Mapping Circle model to Entity model
                    if k.get_circle() != None:
                        debugPrint("found circle %s" % k.get_circle())
                        for l in k.get_circle():
                            entityid = create_entity(bdmlid, component_dbid, measurementid, 'circle')
                            process_coordinates(bdmlid, entityid, l.get_coords(), 'circle', j.get_time(), l.get_radius())
                            create_property(bdmlid, entityid, l.property)

                #Mapping Sphere model to Entity model
                    if k.get_sphere() != None:
                        debugPrint("found sphere")
                        debugPrint("creating entity")
                        spheres_coords = k.get_sphere().get_coords()
                        debugPrint("spheres coords %s" % spheres_coords)
                        # coordinates of spheres; spheres_coords="coordindates of each sphere"
                        #TODO is there more than one coords in spheres_coords?
#                     for spherecoords in spheres_coords:
                        entityid = create_entity(bdmlid, component_dbid, measurementid, 'sphere')
                        debugPrint("sphere: bdmlid %s, entityid %s, spheres_coords %s, time %s, radius %s " % (bdmlid, entityid, spheres_coords, j.get_time(), k.get_sphere().get_radius()))
                        process_coordinates(bdmlid, entityid, spheres_coords, 'sphere', j.get_time(), k.get_sphere().get_radius())
                        propertylist = k.get_sphere().get_property()
                        debugPrint("len(propertylist) %s" % len(propertylist))
                        if len(propertylist) != 0:
                                debugPrint("creating property")
#                               for l in propertylist:
#                                   create_property(bdmlid, entityid, l)
                                create_property(bdmlid, entityid, propertylist)
                        else:
                                debugPrint("no property")

#TODO replicate line to face?
                 #Mapping Face model to Entity model
                    if k.get_face() != None:
                        debugPrint("found face")
                        debugPrint("creating entity")
                        face_coords = k.get_face().get_coords()
                        debugPrint("face coords %s" % face_coords)
                        # coordinates of lines; linecoords="coordindates of each line"
                        for facecoords in face_coords:
                            entityid = create_entity(bdmlid, component_dbid, measurementid, 'face')
                            debugPrint("face: bdmlid %s, entityid %s, facecoords %s, time %s " % (bdmlid, entityid, facecoords, j.get_time() ))
                            process_coordinates(bdmlid, entityid, facecoords, 'face', j.get_time(), None)
#                            if k.get_face().get_property() != None:
                            propertylist = k.get_face().get_property()
                            debugPrint("len(propertylist) %s" % len(propertylist))
                            if len(propertylist) != 0:
                                debugPrint("creating property")
#                               for l in propertylist:
#                                   create_property(bdmlid, entityid, l)
                                create_property(bdmlid, entityid, propertylist)
                            else:
                                debugPrint("no property")
                                
                #Mapping Point model to Entity model
                #checking if it is empty before proceed
                #checking if it is empty before proceed
                    if k.get_point() != None:
                        debugPrint("found point")
                        debugPrint("creating entity")
                        pt_coords = k.get_point().get_coords()
                        debugPrint("Points coords %s" % pt_coords)
                        entityid = create_entity(bdmlid, component_dbid, measurementid, 'point')
                        debugPrint("point: bdmlid %s, entityid %s, coords %s, time %s " % (bdmlid, entityid, pt_coords, j.get_time() ))
                        process_coordinate(bdmlid, entityid, pt_coords, 'point', j.get_time(), None)
                        propertylist = k.get_point().get_property()
                        debugPrint("len(propertylist) %s" % len(propertylist))
                        if len(propertylist) != 0:
                               debugPrint("creating property")
#                               for l in propertylist:
#                                   create_property(bdmlid, entityid, l)
                               create_property(bdmlid, entityid, propertylist)
                        else:
                                debugPrint("no property")
                        debugPrint("creating entity")
                        pt_coords = k.get_point().get_coords()
                        debugPrint("Points coords %s" % pt_coords)
                        entityid = create_entity(bdmlid, component_dbid, measurementid, 'point')
                        debugPrint("point: bdmlid %s, entityid %s, coords %s, time %s " % (bdmlid, entityid, pt_coords, j.get_time() ))
                        process_coordinate(bdmlid, entityid, pt_coords, 'point', j.get_time(), None)
                        propertylist = k.get_point().get_property()
                        debugPrint("len(propertylist) %s" % len(propertylist))
                        if len(propertylist) != 0:
                               debugPrint("creating property")
#                               for l in propertylist:
#                                   create_property(bdmlid, entityid, l)
                               create_property(bdmlid, entityid, propertylist)
                        else:
                                debugPrint("no property")

#TODO replicate sphere to graph?
                #Mapping Graph model to Entity model
                    if k.get_graph() != None:
                        debugPrint("found graph")
                        for l in k.get_graph():
                            entityid = create_entity(bdmlid, component_dbid, measurementid, 'graph')
                            process_coordinates(bdmlid, entityid, l.get_coords(), 'graph', j.get_time(), None)
                            create_property(bdmlid, entityid, l.property)

	print "starting to save bdmldoc"
	ver = "0.15"
	uver = ver.decode('utf-8')
	print("bdmldoc - uver :%s" % uver)
	print("bdmldoc - uver type:%s" % type(uver))
	print("bdmldoc - info:%s" % infoid.id)
	print("bdmldoc - summary:%s" % summaryid.id)
	print("bdmldoc - contact:%s" % contactid.id)
	print("bdmldoc - methods:%s" % methodsid.id)
	print("bdmldoc - data:%s" % dataid.id)
	print("bdmldoc - bdmlid:%s" % bdmlid.id)
#	print("bdmldoc - ownerid:%s" % ownerid.id)
	print("bdmldoc - info:%s, version:%s, summary:%s, contact:%s, methods:%s, data:%s, bdml:%s" % (infoid, uver, summaryid, contactid, methodsid, dataid, bdmlid))
	print("bdmldoc - info.id:%s, version:%s, summary.id:%s, contact.id:%s, methods.id:%s, data.id:%s, bdml.id:%s" % (infoid.id, ver, summaryid.id, contactid.id, methodsid.id, dataid.id, bdmlid.id))
#	print("bdmldoc - info.id:%s, version:%s, summary.id:%s, contact.id:%s, methods.id:%s, data.id:%s, bdml.id:%s, owner.id: %s" % (infoid.id, ver, summaryid.id, contactid.id, methodsid.id, dataid.id, bdmlid.id, ownerid.id))
#	print("bdmldoc - ver type:%s" % type(ver))
#	uver = unicode( ver )
#	print("bdmldoc - uver:%s" % uver)
#	print("bdmldoc - ver type:%s" % type(ver))

        new_bdmldoc = bdmlDocument_model(
            bdml = bdmlid,
#            version = uver,
            info = infoid,
            summary = summaryid,
            contact = contactid,
            methods = methodsid,
            data = dataid,
#            owner = ownerid,
        )
#        new_bdmldoc = bdmlDocument_model(
#            bdml = bdmlid.id,
#            version = uver,
#            info = infoid.id,
#            summary = summaryid.id,
#            contact = contactid.id,
#            methods = methodsid.id,
#            data = dataid.id,
#            owner = ownerid,
#        )
        print("saving (Y) bdmldoc")
        print("bdmldoc: bdml:%s, version:%s, info:%s, summary%s, contact:%s, methods:%s, data:%s" % (new_bdmldoc.bdml, new_bdmldoc.version, new_bdmldoc.info, new_bdmldoc.summary, new_bdmldoc.contact, new_bdmldoc.methods, new_bdmldoc.data))
        new_bdmldoc.save()
        print("bdml file is saved")
        bdmldocid = new_bdmldoc
        print("bdmldoc saved, bdmldocid:%s" %bdmldocid)

        outdata =   {
            'details': "bdml %s is saved in the database" % new_info.bdmlID,
            'error': "none",
        }
    except Exception as e:
        outdata = {
            'details': "%s" % e,
            'error': "cannot save in the database",
        }
    else:
        return outdata
    #debugPrint outdata
    #jsonlist = json.dumps(outdata)
    #return HttpResponse(jsonlist, mimetype='application/javascript; charset=UTF-8')

def create_entity(instance_bdmlid, instance_componentid, instance_measurementid, instance_type):
    debugPrint("creating entity now")
    new_entity = Entity_model(
        bdml = instance_bdmlid,
        component = instance_componentid,
        measurement = instance_measurementid,
        entitytype = instance_type,
    )
    debugPrint("saving entity, component %s, measurement %s, entitytype %s" % (new_entity.component, new_entity.measurement, new_entity.entitytype))
    new_entity.save()
    instance_entityid = new_entity
    debugPrint("entity %s saved" % instance_entityid)
    #   debugPrint l.coordList
    return instance_entityid

def create_property(instance_bdmlid, instance_entityid, instance_propertylist):
    if len(instance_propertylist) != 0:
      debugPrint("propertylist len %s" % len(instance_propertylist))
      for p in instance_propertylist:
        debugPrint("p %s" % p)
        debugPrint("property ref %s, " % p.featureRef)
        debugPrint("feature val  %s, " % p.featureValue)
        debugPrint("entity %s, " % instance_entityid)
        debugPrint("bdml %s, " % instance_bdmlid)
        new_property = Property_model(
            featureRef = p.featureRef,
            featureValue = p.featureValue,
            entity = instance_entityid,
            bdml = instance_bdmlid,
        )
        debugPrint("saving property")
        new_property.save()
        propertyid = new_property
        debugPrint("property %s saved" %propertyid)
#    return propertyid

def process_coordinates(instance_bdmlid, instance_id, instance_coordslist, instance_typeid, instance_time, instance_radius):
    debugPrint("processing coordinates")
    debugPrint("coordslist %s" % instance_coordslist)
    coords = instance_coordslist.split(' ')
    for a in coords:
        debugPrint("a %s" % a)
        b = a.split(',')
        debugPrint("b %s" % b)
        debugPrint("x=%f" % float(b[0]))
        debugPrint("y=%f" % float(b[1]))
        debugPrint("z=%f" % float(b[2]))
        debugPrint("t=%f" % float(instance_time))
        if instance_radius==None:
            new_coord = Coordinates_model(
                    x = float(b[0]),
                    y = float(b[1]),
                    z = float(b[2]),
                    t = float(instance_time),
                    entitytype = instance_typeid,
                    bdml = instance_bdmlid,
                    entity = instance_id,
            )
        else:
            new_coord = Coordinates_model(
                    x = float(b[0]),
                    y = float(b[1]),
                    z = float(b[2]),
                    t = float(instance_time),
                    radius = instance_radius,
                    entitytype = instance_typeid,
                    bdml = instance_bdmlid,
                    entity = instance_id,
            )
        debugPrint("saving coordinate")
        new_coord.save()
        coordid = new_coord
        debugPrint("coordinate %s saved" %coordid)
#    return coordid
#    return coordid

def process_coordinate(instance_bdmlid, instance_id, instance_coords, instance_typeid, instance_time, instance_radius):
    debugPrint("processing coordinates")
    debugPrint("coords %s" % instance_coords)
#    coords = instance_coordslist.split(' ')
#    for a in coords:
#        debugPrint("a %s" % a)
    b = instance_coords[0].split(',')
    debugPrint("b %s" % b)
    debugPrint("x=%f" % float(b[0]))
    debugPrint("y=%f" % float(b[1]))
    debugPrint("z=%f" % float(b[2]))
    debugPrint("t=%f" % float(instance_time))
    if instance_radius==None:
            new_coord = Coordinates_model(
                    x = float(b[0]),
                    y = float(b[1]),
                    z = float(b[2]),
                    t = float(instance_time),
                    entitytype = instance_typeid,
                    bdml = instance_bdmlid,
                    entity = instance_id,
            )
    else:
            new_coord = Coordinates_model(
                    x = float(b[0]),
                    y = float(b[1]),
                    z = float(b[2]),
                    t = float(instance_time),
                    radius = instance_radius,
                    entitytype = instance_typeid,
                    bdml = instance_bdmlid,
                    entity = instance_id,
            )
    debugPrint("saving coordinate")
    new_coord.save()
    coordid = new_coord
    debugPrint("coordinate %s saved" %coordid)
def process_coordinate(instance_bdmlid, instance_id, instance_coords, instance_typeid, instance_time, instance_radius):
    debugPrint("processing coordinates")
    debugPrint("coords %s" % instance_coords)
#    coords = instance_coordslist.split(' ')
#    for a in coords:
#        debugPrint("a %s" % a)
    b = instance_coords[0].split(',')
    debugPrint("b %s" % b)
    debugPrint("x=%f" % float(b[0]))
    debugPrint("y=%f" % float(b[1]))
    debugPrint("z=%f" % float(b[2]))
    debugPrint("t=%f" % float(instance_time))
    if instance_radius==None:
            new_coord = Coordinates_model(
                    x = float(b[0]),
                    y = float(b[1]),
                    z = float(b[2]),
                    t = float(instance_time),
                    entitytype = instance_typeid,
                    bdml = instance_bdmlid,
                    entity = instance_id,
            )
    else:
            new_coord = Coordinates_model(
                    x = float(b[0]),
                    y = float(b[1]),
                    z = float(b[2]),
                    t = float(instance_time),
                    radius = instance_radius,
                    entitytype = instance_typeid,
                    bdml = instance_bdmlid,
                    entity = instance_id,
            )
    debugPrint("saving coordinate")
    new_coord.save()
    coordid = new_coord
    debugPrint("coordinate %s saved" %coordid)
#    return coordid

@csrf_exempt
@transaction.commit_on_success
def qdb_data(request, instance_BDMLID):
    """
    removing bdml data from the database
    : param: instance_BDMLID - bdml's unique ID in BDMLDOCUMENT_Model. Note that it is not the BDML_UUID
    """
    #TODO unfinished - need checking
    if request.method == "DELETE":
        instanceID = bdml_model.objects.filter(id=instance_BDMLID)
        if len(instanceID) == 1:
           debugPrint("found BDML %s" % instanceID)
           Coordinates_model.objects.filter(bdml=instance_BDMLID).delete()
           debugPrint("deleted BDML Coordinates")
           Property_model.objects.filter(bdml=instance_BDMLID).delete()
           debugPrint("deleted BDML Properties")
           Entity_model.objects.filter(bdml=instance_BDMLID).delete()
           debugPrint("deleted BDML Entities")
           Measurement_model.objects.filter(bdml=instance_BDMLID).delete()
           debugPrint("deleted BDML Measurement")
           Component_model.objects.filter(bdml=instance_BDMLID).delete()
           debugPrint("deleted BDML Components")
           Feature_model.objects.filter(bdml=instance_BDMLID).delete()
           debugPrint("deleted BDML Feature")
           Object_model.objects.filter(bdml=instance_BDMLID).delete()
           debugPrint("deleted BDML Object")
           PrevID_model.objects.filter(bdml=instance_BDMLID).delete()
           debugPrint("deleted BDML PrevID")
           Data_model.objects.filter(bdml=instance_BDMLID).delete()
           debugPrint("deleted BDML Data")
           ScaleUnit_model.objects.filter(bdml=instance_BDMLID).delete()
           debugPrint("deleted BDML ScaleType")
           Methods_model.objects.filter(bdml=instance_BDMLID).delete()
           debugPrint("deleted BDML Methods")
           Summary_model.objects.filter(bdml=instance_BDMLID).delete()
           debugPrint("deleted BDML Summary")
           Contact_model.objects.filter(bdml=instance_BDMLID).delete()
           debugPrint("deleted BDML Contact")
           Info_model.objects.filter(bdml=instance_BDMLID).delete()
           debugPrint("deleted BDML Info")
           bdmlDocument_model.objects.filter(id=instance_BDMLID).delete()
           debugPrint("deleted BDML Document")
           bdml_model.objects.filter(id=instance_BDMLID).delete()
           debugPrint("deleted BDML")
           outdata = {'error' : "none", }
        elif len(instanceID) == 0:
           debugPrint("No BDML ID%s found"  %instance_BDMLID)
           outdata = {'error' : "no bdml ID%s found" %instance_BDMLID}
        else:
           debugPrint("error: IDs in database %s" % instanceID)
           outdata = {'error' : "inconsistency in the database, more than 1 ID found? %s" %instance_BDMLID}
    else:
        outdata = {'error' : "wrong method?", }
    debugPrint(outdata)
    jsonlist = json.dumps(outdata)
    return HttpResponse(jsonlist, mimetype='application/javascript; charset=UTF-8')



#TODO create level to control the necessary print statement
def debugPrint(string):
#   if __debug__:
   if myDebug==True:
       print string
   else:
       return
