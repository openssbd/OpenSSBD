from django.db import models
from django.forms import ModelForm


class Contact_model(models.Model):
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

class Info_model(models.Model):
    pdpmlID = models.CharField(max_length=1000, null=True, blank=True)
    title = models.CharField(max_length=1000, null=True, blank=True)
    version = models.IntegerField(null=True, blank=True)
    release = models.DateField(null=True, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class Procedure_model(models.Model):
    name = models.CharField(max_length=1000, null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    step = models.ForeignKey("Step_model")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class Program_model(models.Model):
    name = models.CharField(max_length=1000, null=True, blank=True)
    version = models.CharField(max_length=1000, null=True, blank=True)
    url = models.CharField(max_length=1000, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class Step_model(models.Model):
    name = models.CharField(max_length=1000, null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    annotation = models.CharField(max_length=1000, null=True, blank=True)
    program = models.ForeignKey("Program_model")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class Summary_model(models.Model):
    description = models.CharField(max_length=1000, null=True, blank=True)
    contributors = models.CharField(max_length=1000, null=True, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class pdpmlDocument_model(models.Model):
    version = models.CharField(max_length=1000, null=True, blank=True)
    info = models.ForeignKey("Info_model")
    summary = models.ForeignKey("Summary_model")
    contact = models.ForeignKey("Contact_model")
    procedure = models.ForeignKey("Procedure_model")
    def __unicode__(self):
        return "id: %s" % (self.id, )
