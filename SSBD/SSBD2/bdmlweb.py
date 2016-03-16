from __future__ import unicode_literals
from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.core.servers.basehttp import FileWrapper
from django.db.models import Q, Max, Min, Avg
from SSBD.SSBD2.models import *
from SSBD.SSBD2.bdmlweb_forms import *
from SSBD.BDML.models import *
import re, os, socket

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(search_confs, search_fields, search_keys, request_user, search_flg):
    and_query = None

    while search_keys and search_fields:
        search_conf  = search_confs.pop(0)
        search_field = search_fields.pop(0)
        search_key   = search_keys.pop(0)

        for term in normalize_query(search_key):
            or_query    = None
            fixed_query = None
            if search_field == u'all_fields': # not in
                # except for first field (all_fields)
                for field_name, field_label, model_name in BDML_FIELD_CHOICES[1:]:
                    if not or_query:
                        if field_name == u'bdmlUUID' or field_name == u'schema_ver' or field_name == u'status':
                            or_query = Q(**{"%s__icontains" % (field_name): term})
                        else:
                            or_query = Q(**{"%s__%s__icontains" % (model_name, field_name): term})
                    else:
                        if field_name == u'bdmlUUID' or field_name == u'schema_ver' or field_name == u'status':
                            or_query = or_query | Q(**{"%s__icontains" % (field_name): term})
                        else:
                            or_query = or_query | Q(**{"%s__%s__icontains" % (model_name, field_name): term})

                if not and_query:
                    and_query = or_query
                else:
                    and_query = and_query & or_query
            else:
                model_name = zip(*BDML_FIELD_CHOICES)[2][zip(*BDML_FIELD_CHOICES)[0].index(search_field)]

                if search_conf == 'NOT':
                    if search_field == u'bdmlUUID' or search_field == u'schema_ver' or search_field == u'status':
                        fixed_query = ~Q(**{"%s__icontains" % (search_field): term})
                    else:
                        fixed_query = ~Q(**{"%s__%s__icontains" % (model_name, search_field): term})
                else:
                    if search_field == u'bdmlUUID' or search_field == u'schema_ver' or search_field == u'status':
                        fixed_query = Q(**{"%s__icontains" % (search_field): term})
                    else:
                        fixed_query = Q(**{"%s__%s__icontains" % (model_name, search_field): term})
                if not and_query:
                    and_query = fixed_query
                else:
                    if search_conf == "AND" or search_conf == "NOT":
                        and_query = and_query & fixed_query
                    elif search_conf == "OR":
                        and_query = and_query | fixed_query
    if and_query:
        if search_flg == 0:
            return Q(**{"status__iexact": "available"}) & Q(**{"bdml_multipart_type__exact": "1"}) & and_query # CHECK
            return and_query
        elif search_flg == 1:
            return Q(**{"bdml_multipart_type__exact": "1"}) & and_query # CHECK
    return None

def search(request):
    data = None
    debug = "default";

    if request.method != 'POST':
        formset = SearchFormSet(initial=[{'field': 'all_fields', 'value': '"C. elegans"'}])
    else:
        formset = SearchFormSet(request.POST)
        if not formset.is_valid():
            raise Http404('Invalid request')
        else:
            mode = request.POST.get('form-submit')
            if mode == 'Add':
                formset = SearchFormSet(initial=formset.cleaned_data)
                debug = "add"
            elif mode == 'Search' or mode == 'Next' or mode == 'Previous':
                search_confs  = []
                search_fields = []
                search_keys   = []
                search_flg = 0

                for form in formset.forms: #range(0, formset.total_form_count()):
                    #form = formset.forms[i]
                    search_confs.append(form.cleaned_data['conf'])
                    search_fields.append(form.cleaned_data['field'])
                    search_keys.append(form.cleaned_data['value'])

                    # search available data only when keywords don't include 'bdmlID', and 'schema_ver'
                    if form.cleaned_data['field'] == "bdmlUUID" or form.cleaned_data['field'] == "schema_ver":
                        search_flg = 1;

                entry_query = get_query(search_confs, search_fields, search_keys, request.user, search_flg)
                #debug = entry_query

                if entry_query:
                    data_list = root_model.objects.filter(entry_query).order_by('-schema_ver', 'id') # CHECK
                    debug = data_list.query.__str__() #+ search_flg.__str__()

                    if mode == 'Search':
                        page = int(request.POST.get('page', 1))
                    elif mode == 'Next':
                        page = int(request.POST.get('page', 1)) + 1
                    elif mode == 'Previous':
                        page = int(request.POST.get('page', 1)) - 1
                    else:
                        page = 1

                    paginate_by = 20
                    data_list_p = Paginator(data_list, paginate_by)

                    p = None
                    try:
                        p = data_list_p.page(page)
                    except PageNotAnInteger:
                        p = data_list_p.page(1)
                    except EmptyPage:
                        pass

                    if p != None:
                        data = { 'formset': formset,
                                 'debug': debug if settings.DEBUG else None,
                                 'data_list': p.object_list,
                                 'data_count': data_list.count(), # p.count 
                                 'start_number': p.start_index(),
                                 'end_number': p.end_index(),
                                 'page': page,
                                 'page_number': data_list_p.num_pages,
                                 'has_previous': p.has_previous(),
                                 'previous_page': p.previous_page_number() if p.has_previous() else None,
                                 'has_next': p.has_next(),
                                 'next_page': p.next_page_number() if p.has_next() else None,
                                 }
    if data == None:
        data = { 'formset': formset,
                 'debug': debug if settings.DEBUG else None,
                 'data_list': None,
                 'data_count': 0,
                 }
    return render_to_response('search2.html', context_instance=RequestContext(request, data))

#--------------------------------------------------------------------------------------------------------------

def index(request):
    data = {}

    try:
        data['news_list'] = News_model.objects.all().order_by('-date')[0:2]
    except ObjectDoesNotExist: #Exception:
        data['news_list'] = []

    samples_bdmlID = ['563d487f-1676-4159-a3ab-c25c2e198f6c']
    data['sample_list'] = []
    data['sample_list'].append(('Nuclear division dynamics in C. elegans wild-type embryo',
                                'Kyoda2013.gif',
                                samples_bdmlID[0]))

    data['public_key'] = None
    return render_to_response('index.html', context_instance=RequestContext(request, data))

def news(request):
    data = {}

    try:
        data['news_list'] = News_model.objects.all().order_by('-date')
    except ObjectDoesNotExist: #Exception:
        data['news_list'] = []

    return render_to_response('news.html', context_instance=RequestContext(request, data))

def load_schema(request, filename):
    if filename.startswith('omicsbdml'):
        target_file = os.path.join('/gpfs/www/html/omicsbdml/', filename)
    elif filename.startswith('bdml'):
        target_file = os.path.join('/gpfs/www/html/bdml/', filename)
    elif filename.startswith('pdpml'):
        target_file = os.path.join('/gpfs/www/html/pdpml/', filename)        
    else:
        target_file = "dummary"

    if os.path.exists(target_file):
        return HttpResponse(open(target_file, 'rb').read(), mimetype="application/xml")
    else: raise Http404

def download_bdml(request, projectname, filename):
    target_file = os.path.join('/gpfs/www/html/data/bdml/', projectname, filename)
    if os.path.exists(target_file):
        f = open(target_file, 'rb')
        if filename.endswith('.xml'):
            return HttpResponse(f.read(), mimetype='application/xml')
        elif filename.endswith('.md5'):
            return HttpResponse(f.read(), mimetype='application/md5')
        elif filename.endswith('.zip'):
            response = HttpResponse(FileWrapper(open(target_file, 'rb')), content_type='application/force-download')
            response['Content-Length'] = os.path.getsize(target_file)
            response['Content-Disposition'] = "attachment; filename=%s" % filename
            return response
        else:
            return HttpResponse("test")
    else:
        raise Http404

def download(request, filename):
    target_file = os.path.join('/gpfs/www/html/tools/', filename)
    if os.path.exists(target_file):
        f = open(target_file, 'rb')
        if filename.endswith('.zip') or filename.endswith('.jar'):
            response = HttpResponse(FileWrapper(open(target_file, 'rb')), content_type='application/force-download')
            response['Content-Length'] = os.path.getsize(target_file)
            response['Content-Disposition'] = "attachment; filename=%s" % filename
            return response
        else:
            raise Http404
    else:
        raise Http404

def download_pdpml(request, filename):
    target_file = os.path.join('/gpfs/www/html/data/pdpml/', filename)
    if os.path.exists(target_file):
        f = open(target_file, 'rb')
        if filename.endswith('.xml'):
            return HttpResponse(f.read(), mimetype='application/xml')
        elif filename.endswith('.md5'):
            return HttpResponse(f.read(), mimetype='application/md5')
        else:
            raise Http404
    else:
        raise Http404

# http://stackoverflow.com/questions/8600843/serving-large-files-with-high-loads-in-django
def download_image(request, projectname, filename):
    if filename.endswith('.md5'):
        target_file = os.path.join('/gpfs/www/html/data/source/', projectname, filename)
        f = open(target_file, 'rb')
        return HttpResponse(f.read(), mimetype='application/md5')
    elif filename.endswith('.zip'):
        target_file = os.path.join('/gpfs/www/html/data/source/', projectname, filename)
    else:
        target_file = os.path.join('/gpfs/www/html/data/source/', projectname, filename+'.zip')

    if os.path.exists(target_file):
        response = HttpResponse(FileWrapper(open(target_file, 'rb')), content_type='application/force-download')
        response['Content-Length'] = os.path.getsize(target_file)
        if filename.endswith('.zip'):
            response['Content-Disposition'] = "attachment; filename=%s" % filename
        else:
            response['Content-Disposition'] = "attachment; filename=%s.zip" % filename
        return response
    else: raise Http404

def download_manual(request, filename):
    target_file = os.path.join('/gpfs/www/html/doc/', filename)
    if os.path.exists(target_file):
        f = open(target_file, 'rb')
        response = HttpResponse(open(target_file, 'rb').read(), mimetype="application/pdf")
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response
    else: raise Http404

def download_tools(request, filename):
    target_file = os.path.join('/gpfs/www/html/tools/', filename)
    if os.path.exists(target_file):
        response = HttpResponse(open(target_file, 'rb').read(), mimetype="application/tar.bz2")
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response
    else: raise Http404

def summary(request, uuid):
    data = {}
    debug = ""

    try:
        root = root_model.objects.get(bdmlUUID = uuid)
        data['bdml'] = root
        data['omero'] = None

        data['external_source'] = root.external_source if root.external_source != "" and root.external_source != None else None
        data['internal_source'] = root.internal_source if root.internal_source != "" and root.internal_source != None else None

        data['external_bdml'] = root.external_bdml if root.external_bdml != "" and root.external_bdml != None else None
        data['internal_bdml'] = root.internal_bdml if root.internal_bdml != "" and root.internal_bdml != None else None

        data['external_pdpml'] = root.external_pdpml if root.external_pdpml != "" and root.external_pdpml != None else None
        data['internal_pdpml'] = root.internal_pdpml if root.internal_pdpml != "" and root.internal_pdpml != None else None

        data['link_list'] = []
        data['link_list'] = link_database_model.objects.filter(meta_data_id = root.meta_data).order_by('id')

        data['available'] = True if root.status == 'available' else False

        data['debug'] = debug if settings.DEBUG else None

        return render_to_response('summary2.html', context_instance=RequestContext(request, data))

    except ObjectDoesNotExist:
        raise Http404

def list_dir(request, dirname):
    path = os.path.join('/gpfs/www/html', dirname)
    file_list = sorted(os.listdir(path))
    return render_to_response('directory_index.html', context_instance=RequestContext(request, {'directory': dirname, 'file_list': file_list}))

def history(request, id):
    data = {}
    data['meta_id']   = id
    data['bdml_list'] = root_model.objects.filter(meta_data=id, bdml_multipart_type="1").order_by('-schema_ver') # CHECK
    return render_to_response('history2.html', context_instance=RequestContext(request, data))

class DynamicPageView(TemplateView):
    def get_template_names(self):
        return [self.kwargs['template_name']]

    def get(self, request, *args, **kwargs):
        data = {}
        return render_to_response(self.template_name, data, context_instance=RequestContext(request))

# TODO rewrite as a Object class.
def view4d(request, id):
    try:
        quant = quant_data_model.objects.get(Q(pk = id))
        print quant
    except ObjectDoesNotExist:
        raise Http404()
#    minmax_t = Component_model.objects.filter(bdml_id=id).aggregate(Min('time'))
#    min_t = minmax_t['time__min']
    stats = stats_model.objects.get(bdml=quant.oldbdmlid)
    min_tp = stats.min_tp
    print ("SSBD2: min_tp%s"% min_tp)
#    context = viewer(request, id, min_t)
#    print context
    print "id = %d" % int(id)
    context = viewer(request, id, min_tp)
    return render(request, 'view4d2.html', context)
#    return render(request, 'view4d.html', context)
#    return render(request, 'view4dline.html', context)

def view4dline(request, id):
    try:
        quant = quant_data_model.objects.get(pk = id)
    except ObjectDoesNotExist:
        raise Http404()

#    min_t = stats_model.objects.get(bdml_id=id).min_t
    stats = stats_model.objects.get(bdml=quant.oldbdmlid)
    min_t = stats.min_t
    print ("min_t: %s"% min_t)
    context = viewer(request, id, min_t)
    return render(request, 'view4dline.html', context)

def viewer(request, id, instance_t):
    try:
        quant = quant_data_model.objects.get(pk= id)
        root = root_model.objects.get(quant_data = id, schema_ver=str(0.150))
    except ObjectDoesNotExist:
        raise Http404()
#    minmax_t = Component_model.objects.filter(bdml_id=id).aggregate(Max('time'), Min('time'))
#    max_xyz = Coordinates_model.objects.filter(bdml_id=id).aggregate(

# Counting number of entitities and components directly
#    num_entities = Entity_model.objects.filter(bdml_id=id).count()
#    num_components = Component_model.objects.filter(bdml_id=id).count()
    max_xyz = stats_model.objects.get(bdml=quant.oldbdmlid)
# Counting number of entitities and components using precalculated value in stats_model
    num_components = max_xyz.num_components
    num_entities = max_xyz.num_entities
    scale = ScaleUnit_model.objects.get(bdml_id=quant.oldbdmlid)
    zrange = (max_xyz.max_z-max_xyz.min_z)
    scaleup = 1
#    camx = max_xyz.avg_x*scale.xScale*scaleup
#    camy = max_xyz.avg_y*scale.yScale*scaleup
#    camz = max_xyz.avg_z*scale.zScale*scaleup
    camx = max_xyz.avg_x*scaleup
    camy = max_xyz.avg_y*scaleup
    camz = max_xyz.avg_z*scaleup
    if max_xyz.max_x < 1:
        scaleup = 1/max_xyz.max_z*10
    if max_xyz.avg_x < 1:
        camx = (max_xyz.avg_x)*scale.xScale*scaleup
#        camx = (max_xyz.avg_x)*scaleup
    if max_xyz.avg_y < 1:
        camy = (max_xyz.avg_y)*scale.yScale*scaleup
#        camy = (max_xyz.avg_y)*scaleup
    if max_xyz.avg_z < 1:
        camz = (zrange+max_xyz.avg_z)*scale.zScale*scaleup
#        camz = (zrange+max_xyz.avg_z)*scaleup

    context = {'bdml' : quant,
               'bdmlUUID': root.bdmlUUID,
#               'bdml_id': root.quant_data.id,
               'bdml_id': quant.oldbdmlid,
               'title' : root.meta_data.title,
               'license': root.meta_data.license,
               'description': root.meta_data.description,
               'organism' : root.meta_data.organism,
               'datatype':root.meta_data.datatype,
               'localid':root.meta_data.localid,
               'basedon':root.meta_data.basedon,
               'contributors':root.meta_data.contributors,
               'PMID':root.meta_data.PMID,
               'name':root.meta_data.name,
               'department':root.meta_data.department,
               'organization':root.meta_data.organization,
               'laboratory':root.meta_data.laboratory,
               'method_summary':root.meta_data.method_summary,
               'bdml_path' : root.external_bdml,
               'tunit':root.scaleunit.tUnit,
               'xyzunit':root.scaleunit.xyzUnit,
               't' : instance_t,
               'min_t': max_xyz.min_t,
               'max_t': max_xyz.max_t,
               'min_tp': max_xyz.min_tp,
               'max_tp': max_xyz.max_tp,
#             'tmin' : instance_t,
#             'tmax' : instance_t,
               'cam_x': camx,
               'cam_y': camy,
               'cam_z': camz,
               'avgx' : max_xyz.avg_x,
               'avgy' : max_xyz.avg_y,
               'avgz' : max_xyz.avg_z,
               'xmax' : max_xyz.max_x,
               'ymax' : max_xyz.max_y,
               'zmax' : max_xyz.max_z,
               'xmin' : max_xyz.min_x,
               'ymin' : max_xyz.min_y,
               'zmin' : max_xyz.min_z,
#               'xscale': scale.xScale*scaleup,
#               'yscale': scale.yScale*scaleup,
#               'zscale': scale.zScale*scaleup,
               'xscale': scale.xScale,
               'yscale': scale.yScale,
               'zscale': scale.zScale,
               'tscale': scale.tScale,
               'scaleup' : scaleup,
               'num_components' : num_components,
               'num_entities' : num_entities
               }
    print context['name'];
    return context;

