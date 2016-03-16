from __future__ import unicode_literals
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.core import serializers

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

import pdpmllib    # generateDS generated pdpml interface

# The decorator allows Django to roll back the transaction if the function raises an exception
@transaction.commit_on_success
def read_pdpml(request, filename):
    """
    Reading in a PDPML file and binding its content to pdpml model and save that in the database
    :param request:
    :param filename:
    """
    try:
        pdpmlfile_instance = pdpmllib.parse('/tmp/'+filename)
        checktitle = pdpmlfile_instance.info.title
        checkversion = pdpmlfile_instance.info.version
        checkcontributors = pdpmlfile_instance.summary.contributors
        print "PDPML file: title-%s, version-%s, contributors-%s" %(checktitle, checkversion, checkcontributors)
        dbInfo = Info_model.objects.filter(title=checktitle, version=checkversion)
        if len(dbInfo) != 0: # same title and version found in the existing database {
            print "length of dbInfo %s" %len(dbInfo)
            pdpmldoc = pdpmlDocument_model.objects.filter(info=dbInfo[0].id)
            print "DB pdpmldocid id:%s " % (pdpmldoc[0].id)
            if checkcontributors == Summary_model.objects.get(pdpmldoc[0].summary).contributors:
            # same contributors found in the existing database
                print "DB PDPML contributors %s" % Summary_model.objects.get(pdpmldoc[0].summary).contributors
                print "The same PDPML data (title, version and contributors) exists in the database"
                print "This PDPML file will not be read into the database"
                outdata = {
                    'error' : 'Same PDPML data exists in the database',
                    'PDPML title' : checktitle,
                    'PDPML version' : checkversion,
                    'PDPML contributors' : checkcontributors,
                }
            else: # no contributors match from the database given the title and version
                print "The contributors of this PDPML data file is different from the ones in the database"
                print "Reading the PDPML data into the database"
                outdata = binding_pdpml(pdpmlfile_instance)
                #check to see whether there is any exception error, if there is, then raise exception.
                if outdata['error'] != 'none':
                    raise Exception(outdata)
                print "finishing binding_pdpml 1"
        else:
            print "The version and title of this PDPML does not appear in this database"
            print "Reading the PDPML data into the database"
            outdata = binding_pdpml(pdpmlfile_instance)
            #check to see whether there is any exception error, if there is, then raise exception.
            if outdata['error'] != 'none':
                raise Exception(outdata)
            print "finishing binding pdpml 2"
    except Exception as e:
        outdata = {
            'error': "Cannot save PDPML in the database",
            'details': "%s" % e,
        }
    print outdata
    jsonlist = json.dumps(outdata)
    return HttpResponse(jsonlist, mimetype='application/javascript; charset=UTF-8')

def binding_pdpml(pdpml_instance):
# creating new instances from pdpmlfile and binding it to pdpml model using generateDS
    outdata={}
    try:
        new_contact = Contact_model(
            contactname = pdpml_instance.contact.contactname,
            E_mail = pdpml_instance.contact.E_mail,
            phone = pdpml_instance.contact.phone,
            URL = pdpml_instance.contact.URL,
            organization = pdpml_instance.contact.organization,
            department = pdpml_instance.contact.department,
            laboratory = pdpml_instance.contact.laboratory,
            address = pdpml_instance.contact.address,
        )
        new_info = Info_model(
            pdpmlID = pdpml_instance.info.pdpmlID,
            title = pdpml_instance.info.title,
            date = pdpml_instance.info.date,
            version = pdpml_instance.info.version,
        )
        new_procedure = Procedure_model(
            name = pdpml_instance.procedure.name,
            order = pdpml_instance.procedure.order,
            description = pdpml_instance.procedure.description,
            step = pdpml_instance.procedure.step,
        )
        new_program = Program_model(
            name = pdpml_instance.program.name,
            version = pdpml_instance.program.version,
            url = pdpml_instance.program.url,
            description = pdpml_instance.program.description,
        )
        new_step = Step_model(
            name = pdpml_instance.step.name,
            order = pdpml_instance.step.order,
            annotation = pdpml_instance.step.annotation,
            program = pdpml_instance.step.program,
        )
        new_summary = Summary_model(
            description = pdpml_instance.summary.description,
            contributors = pdpml_instance.summary.contributors,
        )
        data = {
            'error' : 'none',
            'contact.contactname' : new_contact.contactname,
            'contact.E_mail' : new_contact.E_mail,
            'contact.phone' : new_contact.phone,
            'contact.URL' : new_contact.URL,
            'contact.organization' : new_contact.organization,
            'contact.department' : new_contact.department,
            'contact.laboratory' : new_contact.laboratory,
            'contact.address' : new_contact.address,
            'Info.pdpmlID' : new_info.pdpmlID,
            'Info.title' : new_info.title,
            'Info.version' : new_info.version,
            'Info.date' : new_info.date,
        }
        print "saving contacts"
        new_contact.save()
        contactid = new_contact
        print "contacts %s saved" % contactid
        print "saving info"
        new_info.save()
        infoid = new_info
        print "info %s saved" % infoid
        print "saving procedure"
        new_procedure.save()
        procedureid = new_procedure
        print "procedure %s saved" % procedureid
        print "saving program"
        new_program.save()
        programid = new_program
        print "program %s saved" % procedureid
        print "saving step"
        new_step.save()
        stepid = new_step
        print "step %s saved" % stepid
        print "saving summary"
        new_summary.save()
        summaryid = new_summary
        print "summary %s saved" % summaryid

        new_pdpmldoc = pdpmlDocument_model(
            version = pdpml_instance.pdpmldocument.version,
            level = pdpml_instance.pdpmldocument.level,
            info = infoid,
            summary = summaryid,
            contact = contactid,
            procedure = procedureid,
        )
        print "saving pdpmldocument"
        new_pdpmldoc.save()
        pdpmldocid = new_pdpmldoc
        print "pdpmldocument %s saved" % pdpmldocid
        data = {
            'error' : "none",
            'data'    : "%s" %data,
        }
    except Exception as e:
        data = {
            'error' : "cannot save in the database",
            'details' : "%s" %e,
            'data'    : "%s" %data,
        }
    else:
        return outdata


