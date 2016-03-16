# -*- coding: utf-8 -*-
"""
SSBD Internal Data Model
based on BDML version 0.15
"""
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import UserManager, AbstractBaseUser, BaseUserManager

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

class root_model(models.Model):
    bdml_multipart = models.ForeignKey('bdml_multipart_model')
    bdml_multipart_type = models.CharField(max_length=1000, null=True, blank=True) # type of bdmlfile, multipart
    meta_data = models.ForeignKey('meta_data_model')
    quant_data = models.ForeignKey('quant_data_model', null=True, blank=True)
    scaleunit = models.ForeignKey('ScaleUnit_model', null=True, blank=True)
    omero_datasetID  = models.IntegerField(null=True, blank=True)
#    omero = models.ForeignKey('Omero_model')
    owner = models.ForeignKey('Owner_model')
    schema_ver = models.DecimalField(max_digits=5, decimal_places=3)
    bdmlUUID = models.CharField(max_length=1000, unique=True)
    localid = models.CharField(max_length=1000) # i.e. localID
    release = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1000)
    external_bdml   = models.CharField(max_length=100, null=True, blank=True)  # new - do we need it?
    external_pdpml = models.CharField(max_length=1000, null=True, blank=True) # copy from method model
    external_source = models.CharField(max_length=1000, null=True, blank=True)
    internal_bdml   = models.CharField(max_length=100, null=True, blank=True) # copy from web path
    internal_pdpml  = models.CharField(max_length=100, null=True, blank=True)# copy from web path
    internal_source  = models.CharField(max_length=100, null=True, blank=True)# copy from web path image
#    version = models.IntegerField() # i.e. version ??
    def __unicode__(self):
        return "id: %s" % (self.id, )

class bdml_multipart_model(models.Model):
    bdmlUUID = models.CharField(max_length=1000, null=True, blank=True)
    localid = models.CharField(max_length=1000) # i.e. localID
    type = models.CharField(max_length=1000, null=True, blank=True) # type of bdmlfile, multipart
    oldbdmlid = models.IntegerField(null=True, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )


#class bdmlDocument_model(models.Model):
#    bdml = models.ForeignKey("bdml_model")
#    version = models.CharField(max_length=1000, null=True, blank=True)
#    info = models.ForeignKey("Info_model")
#    summary = models.ForeignKey("Summary_model")
#    contact = models.ForeignKey("Contact_model")
#    methods = models.ForeignKey("Methods_model")
#    data = models.ForeignKey("Data_model")
#    owner  = models.ForeignKey(Owner_model) # user auth
#    update = models.ForeignKey("Update_model")
#    def __unicode__(self):
#        return "id: %s" % (self.id, )
#    class Meta:
#         app_label="classes"

class meta_data_model(models.Model):
    name            = models.CharField(max_length=1000, null=True, blank=True)
    E_mail          = models.CharField(max_length=1000, null=True, blank=True)
    phone           = models.CharField(max_length=1000, null=True, blank=True)
    URL             = models.CharField(max_length=1000, null=True, blank=True)
    organization    = models.CharField(max_length=1000, null=True, blank=True)
    department      = models.CharField(max_length=1000, null=True, blank=True)
    laboratory      = models.CharField(max_length=1000, null=True, blank=True)
    address         = models.CharField(max_length=1000, null=True, blank=True)
    title           = models.CharField(max_length=1000, null=True, blank=True)
    description     = models.CharField(max_length=1000, null=True, blank=True)
    organism        = models.CharField(max_length=1000, null=True, blank=True)
    datatype        = models.CharField(max_length=1000, null=True, blank=True)
    localid         = models.CharField(max_length=1000, null=True, blank=True)  # used to be called identifier
    basedon         = models.CharField(max_length=1000, null=True, blank=True)
    contributors    = models.CharField(max_length=1000, null=True, blank=True)
    citation        = models.CharField(max_length=1000, null=True, blank=True)
    PMID            = models.IntegerField(null=True, blank=True)
    dblink          = models.CharField(max_length=1000, null=True, blank=True)
    license         = models.CharField(max_length=1000, null=True, blank=True)
    method_summary  = models.CharField(max_length=1000, null=True, blank=True)
    orf             = models.CharField(max_length=20, null=True, blank=True)
    gene            = models.CharField(max_length=20, null=True, blank=True)
    oldbdmlid = models.IntegerField(null=True, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

# quant_data_model is based on BDML Data_model
class quant_data_model(models.Model):
#    scaleUnit= models.ForeignKey('ScaleUnit_model')
    localid = models.CharField(max_length=1000) # i.e. localID is the only identifier available to distinguish different set of data
    oldbdmlid = models.IntegerField(null=True, blank=True)
#    scaleUnit = models.ForeignKey('ScaleUnit_model')
#    componentID = models.CharField(max_length=1000)
#    componentName = models.CharField(max_length=1000, null=True, blank=True)
#    time = models.FloatField()
#    groupID = models.CharField(max_length=1000)
#    objectName = models.CharField(max_length=1000, null=True, blank=True)
#    objectRef = models.CharField(max_length=1000, blank=True)
#    entitytype = models.CharField(ENTITYTYPES.items(), max_length=80)
#    feature = models.ForeignKey("Feature_model")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class Path_model(models.Model):
    bdmlID = models.CharField(max_length=160)
    bdml   = models.CharField(max_length=100, blank=True)
    pdpml  = models.CharField(max_length=100, blank=True)
    image  = models.CharField(max_length=100, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class Omero_model(models.Model):
    root     = models.ForeignKey('root_model')
    datasetID  = models.IntegerField()
    def __unicode__(self):
        return "id: %s" % (self.id, )

class link_database_model(models.Model):
    meta_data = models.ForeignKey('meta_data_model')
    database  = models.CharField(max_length=100) # Ensembl             WormBase
    URL       = models.CharField(max_length=300) # http://...          http://...
    symbol    = models.CharField(max_length=200, null=True, blank=True) # ENSMUSG00000030735  B0336.10
    category  = models.CharField(max_length=200, null=True, blank=True) # homologous_gene     gene
    organism  = models.CharField(max_length=200, null=True, blank=True) # mus_musculus        caenorhabditis_elegans
    gene      = models.CharField(max_length=200, null=True, blank=True) # mus_musculus        caenorhabditis_elegans

    def __unicode__(self):
        return "id: %s, name: %s" % (self.id, self.name)

class News_model(models.Model):
    date  = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=50)
    text  = models.TextField()
    def __unicode__(self):
        return "id: %s" % (self.id, )

class Owner_model(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254, unique=False)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    phone = models.SlugField(max_length=30, null=True, blank=True)
    URL = models.CharField(max_length=200, null=True, blank=True)
    organization = models.CharField(max_length=200, null=True, blank=True)
    department = models.CharField(max_length=200, null=True, blank=True)
    laboratory = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])

    def __unicode__(self):
        return self.username

    @property
    def is_staff(self):
        return False

    def is_anonymous(self):
        return False

class Entity_model(models.Model):
#    bdml = models.ForeignKey('bdml_model')
    quant_data = models.ForeignKey('quant_data_model')
    measurement = models.ForeignKey('Measurement_model')
    component = models.ForeignKey('Component_model')
#    object = models.ForeignKey('Object_model')
#    property = models.ForeignKey('Property_model', null=True, blank=True)
    entitytype = models.CharField(ENTITYTYPES.items(), max_length=80)
    oldentityid = models.IntegerField()
    def __unicode__(self):
        return "id: %s" % (self.id, )

class Feature_model(models.Model):
    quant_data = models.ForeignKey('quant_data_model')
    featureName = models.CharField(max_length=1000, null=True, blank=True)
    featureScale = models.FloatField(null=True, blank=True)
    featureUnit = models.CharField(max_length=1000, null=True, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

#class Entity_model(models.Model):
#    quantdata = models.ForeignKey('quantdata_model')
#    measurement = models.ForeignKey('Measurement_model')
#    entitytype = models.CharField(ENTITYTYPES.items(), max_length=80)
#    def __unicode__(self):
#        return "id: %s" % (self.id, )

class Coordinates_model(models.Model):
    quant_data = models.ForeignKey('quant_data_model')
#    bdml = models.ForeignKey('bdml_model')
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    t = models.FloatField(null=True, blank=True)
    radius = models.FloatField(null=True, blank=True)
    entitytype = models.CharField(ENTITYTYPES.items(), max_length=80)
    entity = models.ForeignKey('Entity_model')
#    object = models.ForeignKey('Object_model')
    measurement = models.ForeignKey('Measurement_model')
    component = models.ForeignKey('Component_model')
    def __unicode__(self):
        return "id: %s" % (self.id, )

# unicoords means unified coordinates. It allows easier analysis of coordinates data as well as for display.
# current implementation unified coordinates based on micrometers and seconds for t.

class unicoords_model(models.Model):
    quant_data = models.ForeignKey('quant_data_model')
#    bdml = models.ForeignKey('bdml_model')
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
#    entity = models.ForeignKey('Entity_model')
    measurement = models.ForeignKey('Measurement_model')
    component = models.ForeignKey('Component_model')
#    summary = models.ForeignKey('Summary_model')
#    info = models.ForeignKey('Info_model')
    def __unicode__(self):
        return "id: %s" % (self.id, )

class stats_model(models.Model):
    quant_data = models.ForeignKey('quant_data_model')
#    bdml = models.ForeignKey('bdml_model')
#    info = models.ForeignKey('Info_model')
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
    max_pt = models.FloatField()
    min_pt = models.FloatField()
    timestep = models.FloatField()
#    num_entities = models.IntegerField()
#    num_components = models.IntegerField()
    def __unicode__(self):
        return "id: %s" % (self.id, )

class compstats_model(models.Model):
    quant_data = models.ForeignKey('quant_data_model')
#    bdml_id = models.IntegerField()
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

    def __unicode__(self):
        return "id: %s" % (self.id, )

class Component_model(models.Model):
    quant_data = models.ForeignKey('quant_data_model')
#    bdml = models.ForeignKey('bdml_model')
    componentID = models.CharField(max_length=1000)
    componentName = models.CharField(max_length=1000, null=True, blank=True)
    time = models.FloatField()
    oldcomponentid = models.IntegerField()
#    data = models.ForeignKey("Data_model")
#    groupID = models.CharField(max_length=1000, null=True, blank=True)
#    prevID = models.CharField(max_length=1000, null=True, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class Measurement_model(models.Model):
    quant_data = models.ForeignKey('quant_data_model')
#    bdml = models.ForeignKey('bdml_model')
    component = models.ForeignKey('Component_model')
    objectRef = models.CharField(max_length=1000, blank=True)
    object = models.ForeignKey('Object_model', null=True, blank=True)
    oldmeasurementid = models.IntegerField()
#    entity = models.ForeignKey('Entity_model')
#    point = models.ForeignKey("Point_model")
#    line = models.ForeignKey("Line_model")
#    face = models.ForeignKey("Face_model")
#    circle = models.ForeignKey("Circle_model")
#    sphere = models.ForeignKey("Sphere_model")
#    graph = models.ForeignKey("Graph_model")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class Object_model(models.Model):
    quant_data = models.ForeignKey('quant_data_model')
#    bdml = models.ForeignKey('bdml_model')
    objectName = models.CharField(max_length=1000, null=True, blank=True)
#    measurement = models.ForeignKey('Measurement_model')
#    component = models.ForeignKey('Component_model')
#    data = models.ForeignKey('Data_model')
    def __unicode__(self):
        return "id: %s" % (self.id, )

class PrevID_model(models.Model):
    quant_data = models.ForeignKey('quant_data_model')
#    bdml = models.ForeignKey('bdml_model')
    component = models.ForeignKey('Component_model')
#    data = models.ForeignKey('Data_model')
    prevID = models.CharField(max_length=1000)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class Property_model(models.Model):
    featureRef = models.CharField(max_length=1000, null=True, blank=True)
    featureValue = models.CharField(max_length=1000, null=True, blank=True)
#    bdml = models.ForeignKey("bdml_model")
    quant_data = models.ForeignKey('quant_data_model')
    entity = models.ForeignKey('Entity_model')
#    object = models.ForeignKey("Object_model", null=True, blank=True)
#    measurement = models.ForeignKey('Measurement_model')
#    component = models.ForeignKey('Component_model')
    def __unicode__(self):
        return "id: %s" % (self.id, )

class ScaleUnit_model(models.Model):
#    quant_data = models.ForeignKey('quant_data_model', null=True, blank=True)
    quant_data = models.ForeignKey('quant_data_model')
#    bdml = models.ForeignKey("bdml_model")
    xScale = models.FloatField(null=True, blank=True)
    yScale = models.FloatField(null=True, blank=True)
    zScale = models.FloatField(null=True, blank=True)
    xyzUnit = models.CharField(UNITS.items(), max_length=1000, null=True, blank=True)
    tScale = models.FloatField(null=True, blank=True)
    tUnit = models.CharField(TUNITS.items(), max_length=1000, null=True, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )
