# -*- coding: utf-8 -*-
"""
SSBD Internal Data Model
based on BDML version 0.15
"""
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

ENTITYTYPES = {
     'line' : 'line object',
     'point' : 'point object',
     'face' : 'face object',
     'circle' : 'circle object',
     'sphere' : 'sphere object',
     'graph' : 'graph object',
}

UNITS = {
        'ampere' : 'A',
        'candela' : 'cd',
        'celsius' : '\C',
        'coulomb' : 'C',
        'dimensionless' : 'dimensionless',
        'farad' : 'F',
        'gram' : 'g',
        'gray' : 'Gy',
        'henry' : 'H',
        'hertz' : 'Hz',
        'intensity' : 'intensity',
        'item' : 'item',
        'joule' : 'J',
        'katal' : 'kat',
        'kelvin' : 'K',
        'kilogram' : 'Kg',
        'liter' : 'L',
        'litre' : 'L',
        'lumen' : 'lm',
        'lux' : 'lx',
        'meter' : 'm',
        'metre' : 'm',
        'micrometer' : 'm',
        'micrometre' : 'm',
        'mole' : 'mol',
        'newton' : 'N',
        'ohm' : 'ohm',
        'pascal' : 'Pa',
        'pixel' : 'pixel',
        'radian' : 'rad',
        'relative' : 'relative',
        'siemens' : 'S',
        'sievert' : 'Sv',
        'steradian' : 'sr',
        'tesla' : 'T',
        'volt' : 'V',
        'watt' : 'W',
        'weber' : 'Wb'
}

TUNITS = {
        'nanosecond' : 'ns',
        'microsecond' : 's',
        'millisecond' : 'ms',
        'second' : 's',
        'minute' : 'min',
        'hour' : 'h',
        'day' : 'd',
        'month' : 'month',
        'year' : 'yr',
}


class Component_model(models.Model):
    bdml = models.ForeignKey('bdml_model')
    componentID = models.CharField(max_length=1000)
    componentName = models.CharField(max_length=1000, null=True, blank=True)
    time = models.FloatField()
    data = models.ForeignKey("Data_model")
#    groupID = models.CharField(max_length=1000, null=True, blank=True)
#    prevID = models.CharField(max_length=1000, null=True, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class Contact_model(models.Model):
    bdml = models.ForeignKey('bdml_model')
    name = models.CharField(max_length=1000, null=True, blank=True)
    E_mail = models.CharField(max_length=1000, null=True, blank=True)
    phone = models.CharField(max_length=1000, null=True, blank=True)
    URL = models.CharField(max_length=1000, null=True, blank=True)
    organization = models.CharField(max_length=1000, null=True, blank=True)
    department = models.CharField(max_length=1000, null=True, blank=True)
    laboratory = models.CharField(max_length=1000, null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class Data_model(models.Model):
    bdml = models.ForeignKey('bdml_model')
    scaleUnit = models.ForeignKey('ScaleUnit_model')
#    object = models.ForeignKey("Object_model")
#    feature = models.ForeignKey("Feature_model")
#    component = models.ForeignKey("Component_model")
    def __unicode__(self):
        return "id: %s" % (self.id, )


class Feature_model(models.Model):
    bdml = models.ForeignKey('bdml_model')
    data = models.ForeignKey('Data_model')
    featureName = models.CharField(max_length=1000, null=True, blank=True)
    featureScale = models.FloatField(null=True, blank=True)
    featureUnit = models.CharField(max_length=1000, null=True, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class GroupID_model(models.Model):
    bdml = models.ForeignKey('bdml_model')
    component = models.ForeignKey('Component_model')
    data = models.ForeignKey('Data_model')
    groupID = models.CharField(max_length=1000)
    def __unicode__(self):
        return "id: %s" % (self.id, )


class Info_model(models.Model):
    bdml = models.ForeignKey("bdml_model")
    bdmlID = models.CharField(max_length=1000, null=True, blank=True)
    title = models.CharField(max_length=1000, null=True, blank=True)
    version = models.IntegerField(null=True, blank=True)
    release = models.DateField(null=True, blank=True)
    license = models.CharField(max_length=1000, null=True, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )
#    class Meta:
#         app_label="classes"


class Entity_model(models.Model):
    bdml = models.ForeignKey('bdml_model')
    measurement = models.ForeignKey('Measurement_model')
    component = models.ForeignKey('Component_model')
#    object = models.ForeignKey('Object_model')
#    property = models.ForeignKey('Property_model', null=True, blank=True)
    entitytype = models.CharField(ENTITYTYPES.items(), max_length=80)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class Update_model(models.Model):
    ssbd_id = models.CharField(max_length=1000)
    data_id = models.IntegerField()
    version = models.IntegerField() # i.e. version within a BDML file
    schema = models.DecimalField(max_digits=5, decimal_places=3)
    bdmlUUID = models.CharField(max_length=1000, unique=True)
    localid = models.CharField(max_length=1000) # i.e. localID
    source = models.CharField(max_length=1000, null=True, blank=True)
    status = models.CharField(max_length=1000)
    fk = models.ForeignKey('bdmlDocument_model')
    def __unicode__(self):
        return "id: %s" % (self.id, )

class Coordinates_model(models.Model):
    bdml = models.ForeignKey('bdml_model')
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    t = models.FloatField(null=True, blank=True)
    radius = models.FloatField(null=True, blank=True)
    entitytype = models.CharField(ENTITYTYPES.items(), max_length=80)
    entity = models.ForeignKey('Entity_model')
#    object = models.ForeignKey('Object_model')
#    measurement = models.ForeignKey('Measurement_model')
#    component = models.ForeignKey('Component_model')
    def __unicode__(self):
        return "id: %s" % (self.id, )

# unicoords means unified coordinates. It allows easier analysis of coordinates data as well as for display.
# current implementation unified coordinates based on micrometers and seconds for t.
class unicoords_model(models.Model):
    bdml = models.ForeignKey('bdml_model')
    coords = models.ForeignKey('Coordinates_model')
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    t = models.FloatField(null=True, blank=True)
    timept = models.FloatField(null=True, blank=True)
#    x = models.IntegerField()
#    y = models.IntegerField()
#    z = models.IntegerField()
#    t = models.IntegerField(null=True, blank=True)
    radius = models.FloatField(null=True, blank=True)
#  um means micrometers is used to denote the scale in x, y, z in terms of micrometers.
#  If the um is 10, it means that x is in um*x micrometer, i.e. 10 micrometers
#    um = models.FloatField()
    entitytype = models.CharField(ENTITYTYPES.items(), max_length=80)
    entity = models.ForeignKey('Entity_model')
    measurement = models.ForeignKey('Measurement_model')
    component = models.ForeignKey('Component_model')
    summary = models.ForeignKey('Summary_model')
    info = models.ForeignKey('Info_model')
    def __unicode__(self):
        return "id: %s" % (self.id, )

class stats_model(models.Model):
    bdml = models.ForeignKey('bdml_model')
    info = models.ForeignKey('Info_model')
    max_x = models.FloatField()
    min_x = models.FloatField()
    avg_x = models.FloatField()
    max_y = models.FloatField()
    min_y = models.FloatField()
    avg_y = models.FloatField()
    max_z = models.FloatField()
    min_z = models.FloatField()
    avg_z = models.FloatField()
    max_t = models.FloatField()
    min_t = models.FloatField()
    max_tp = models.FloatField()
    min_tp = models.FloatField()
    num_entities = models.IntegerField()
    num_components = models.IntegerField()
#    timestep = models.FloatField()
    def __unicode__(self):
        return "id: %s" % (self.id, )

class compstats_model(models.Model):
    bdml_id = models.IntegerField()
    max_x = models.FloatField()
    min_x = models.FloatField()
    avg_x = models.FloatField()
    max_y = models.FloatField()
    min_y = models.FloatField()
    avg_y = models.FloatField()
    max_z = models.FloatField()
    min_z = models.FloatField()
    avg_z = models.FloatField()
    measurement_id = models.IntegerField()
    component_id = models.IntegerField()
    t = models.FloatField()
    tp = models.FloatField()
    def __unicode__(self):
        return "id: %s" % (self.id, )

class Update_model(models.Model):
#    bdml_id = models.IntegerField(unique=True)
    ssbd_id = models.CharField(max_length=1000)
    data_id = models.IntegerField()
    version = models.IntegerField() # i.e. version within a BDML file
    schema = models.DecimalField(max_digits=5, decimal_places=3)
    bdmlUUID = models.CharField(max_length=1000, unique=True)
    localid = models.CharField(max_length=1000) # i.e. localID
    source = models.CharField(max_length=1000, null=True, blank=True)
    pdpml = models.CharField(max_length=1000, null=True, blank=True)
    status = models.CharField(max_length=1000)
    def __unicode__(self):
        return "id: %s" % (self.id, )


class Measurement_model(models.Model):
    bdml = models.ForeignKey('bdml_model')
    component = models.ForeignKey('Component_model')
    objectRef = models.CharField(max_length=1000, blank=True)
    object = models.ForeignKey('Object_model', null=True, blank=True)
#    entity = models.ForeignKey('Entity_model')
#    point = models.ForeignKey("Point_model")
#    line = models.ForeignKey("Line_model")
#    face = models.ForeignKey("Face_model")
#    circle = models.ForeignKey("Circle_model")
#    sphere = models.ForeignKey("Sphere_model")
#    graph = models.ForeignKey("Graph_model")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class Methods_model(models.Model):
    bdml = models.ForeignKey('bdml_model')
    summary = models.CharField(max_length=1000, null=True, blank=True)
    source = models.CharField(max_length=1000, null=True, blank=True)
    pdpml = models.CharField(max_length=1000, null=True, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class Object_model(models.Model):
    bdml = models.ForeignKey('bdml_model')
    objectName = models.CharField(max_length=1000, null=True, blank=True)
#    measurement = models.ForeignKey('Measurement_model')
#    component = models.ForeignKey('Component_model')
    data = models.ForeignKey('Data_model')
    def __unicode__(self):
        return "id: %s" % (self.id, )

class PrevID_model(models.Model):
    bdml = models.ForeignKey('bdml_model')
    component = models.ForeignKey('Component_model')
    data = models.ForeignKey('Data_model')
    prevID = models.CharField(max_length=1000)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class Property_model(models.Model):
    featureRef = models.CharField(max_length=1000, null=True, blank=True)
    featureValue = models.CharField(max_length=1000, null=True, blank=True)
    bdml = models.ForeignKey("bdml_model")
    entity = models.ForeignKey('Entity_model')
#    object = models.ForeignKey("Object_model", null=True, blank=True)
#    measurement = models.ForeignKey('Measurement_model')
#    component = models.ForeignKey('Component_model')
    def __unicode__(self):
        return "id: %s" % (self.id, )

class ScaleUnit_model(models.Model):
    bdml = models.ForeignKey("bdml_model")
    xScale = models.FloatField(null=True, blank=True)
    yScale = models.FloatField(null=True, blank=True)
    zScale = models.FloatField(null=True, blank=True)
    xyzUnit = models.CharField(UNITS.items(), max_length=1000, null=True, blank=True)
    tScale = models.FloatField(null=True, blank=True)
    tUnit = models.CharField(TUNITS.items(), max_length=1000, null=True, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class Summary_model(models.Model):
    bdml = models.ForeignKey("bdml_model")
    description = models.CharField(max_length=1000, null=True, blank=True)
    organism = models.CharField(max_length=1000, null=True, blank=True)
    datatype = models.CharField(max_length=1000, null=True, blank=True)
    identifier = models.CharField(max_length=1000, null=True, blank=True)
    basedon = models.CharField(max_length=1000, null=True, blank=True)
    contributors = models.CharField(max_length=1000, null=True, blank=True)
    citation = models.CharField(max_length=1000, null=True, blank=True)
    PMID = models.IntegerField(null=True, blank=True)
    dblink = models.CharField(max_length=1000, null=True, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class bdmlDocument_model(models.Model):
    bdml = models.ForeignKey("bdml_model")
    version = models.CharField(max_length=1000, null=True, blank=True)
    info = models.ForeignKey("Info_model")
    summary = models.ForeignKey("Summary_model")
    contact = models.ForeignKey("Contact_model")
    methods = models.ForeignKey("Methods_model")
    data = models.ForeignKey("Data_model", null=True, blank=True)
#    update = models.ForeignKey("Update_model")
    def __unicode__(self):
        return "id: %s" % (self.id, )
#    class Meta:
#         app_label="classes"

# a dummy model for internal reference used.
class bdml_model(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    bdml_ID = models.CharField(max_length=1000, null=True, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )
