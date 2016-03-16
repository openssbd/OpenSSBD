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
# for User login
#from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import PasswordChangeForm
#
from SSBD.SSBD2.models import *
from SSBD.SSBD2.bdmlweb_forms import *
from SSBD.BDML.models import *
import re, os, socket

#----- related search form

def infix2query (command):
    list_data = []

    sql_head = r'SELECT "SSBD2_root_model"."id", "SSBD2_root_model"."meta_data_id", "SSBD2_root_model"."schema_ver", "SSBD2_root_model"."bdmlUUID", "SSBD2_root_model"."localid", "SSBD2_root_model"."status" FROM "SSBD2_root_model" INNER JOIN "SSBD2_meta_data_model" ON ("SSBD2_root_model"."meta_data_id" = "SSBD2_meta_data_model"."id") WHERE ( "SSBD2_root_model"."bdml_multipart_type"=%s and ' # CHECK
    sql_tail = r' ) ORDER BY "SSBD2_root_model"."schema_ver" DESC, "SSBD2_root_model"."id" ASC'

    command_upper = command.upper()

    list_data.append('1') # CHECK

    sql = re.sub(r'\s+[nN][oO][tT]\s+', r' AND NOT ', command_upper)
    match = re.findall(r"(([\w\.\-][\w\.\-\(\)]+[\w\.\-]|\"[^\"]+\"|[0-9]\.[0-9]+)\s*\[([^\[\]]+)\])", sql)

    for subseq, key, conf in match:
        mm = re.match(r"\"(.+)\"", key)
        if mm:
            key = mm.group(1)

        if conf == 'PMID' or conf == 'SCHEMA': # 'schema' is changed into capital
            upperseq = BDML_TABLE_DICT[conf] + r'=' + key
        else:
            upperseq = r'UPPER(' + BDML_TABLE_DICT[conf] + r') LIKE UPPER(%s)'
            list_data.append('%' + key.upper() + '%')

#       upperseq = r'UPPER(' + BDML_TABLE_DICT[conf.upper()] + r') LIKE UPPER(%s)'
        sql = sql.replace(subseq, upperseq, 1)
    
    return sql_head + sql + sql_tail, tuple(list_data)

def query2infix (query):
    command = ""
    r = re.compile('(WHERE|AND|OR|AND NOT)\s\(*?UPPER\(\s+\"([A-Z0-9]+)_([A-Z0-9]+)\"\.\"([A-Z0-9]+)\"\) LIKE\s+%(\S+)%\s+')
    for conf, t1, t2, t3, w in r.findall(query):
        if conf == 'WHERE':
            tmp = "%s_%s_%s = %s" % (t1, t2, t3, w)
        else:
            tmp = " %s %s_%s_%s = %s" % (conf, t1, t2, t3, w)
        command += tmp
#    return command
    return  query

def get_data_from_simple_form(request):
    data = None
    debug = "default"
    state = ""
    sql = ""

    if request.method == 'GET':
        form = SimpleSearchForm(request.GET)
        if form.is_valid():
            mode = request.GET.get('form-submit')
            if mode == 'Search' or mode == 'Next' or mode == 'Previous':
                sql, tuple_data = infix2query(form.cleaned_data['value'])
                try:
                    data_list = list(root_model.objects.raw(sql, tuple_data))
                    state = "search_success"
                except:
                    data_list = []
                    state = "search_fail"

                debug = state + ": " + sql + "(" +  ",".join(tuple_data) + ")"

                paginate_by = 20
                data_list_p = Paginator(data_list, paginate_by)

                page = 1
                if mode == 'Search':
                    page = int(request.GET.get('page', 1))
                elif mode == 'Next':
                    page = int(request.GET.get('page', 1)) + 1
                elif mode == 'Previous':
                    page = int(request.GET.get('page', 1)) - 1

                p = None
                try:
                    p = data_list_p.page(page)
                except PageNotAnInteger:
                    p = data_list_p.page(1)
                except EmptyPage:
                    pass

                if p != None:
                    data = { 'form': form,
                             'state': state,
                             'debug': debug if settings.DEBUG else None,
                             'data_list': p.object_list,
                             'data_count': len(data_list),
                             
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
        data = { 'form': SimpleSearchForm(initial={'value': '"C. elegans" [organism] and RNAi [description]'}),
                 'state': '', 
                 'debug': debug if settings.DEBUG else None,
                 'data_list': None,
                 'data_count': 0,
                 }        
    return data

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(search_confs, search_fields, search_keys, request_user, search_flg):
    #if request_user.is_anonymous() or request_user.username == settings.SSBD_ADMIN:
    #    login_user = Owner_model.objects.get(username__exact=settings.SSBD_PUBLIC)
    #else:
    #    login_user = request_user

    and_query = None #Q(owner = login_user)

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
    data = get_data_from_simple_form(request)
    if data['state'] == "search_success" or data['state'] == "search_fail":
        return render_to_response('search_simple2.html', context_instance=RequestContext(request, data))

    try:
        data['news_list'] = News_model.objects.all().order_by('-date')[0:2]
    except ObjectDoesNotExist: #Exception:
        data['news_list'] = []

    samples_bdmlID = ['cfeeedb0-5e3e-44ee-969a-1c7d40a4d98b', 'afc304bc-7cca-4c92-8764-f5957dd06e3d', 'FF452590-EAE4-11E3-85C9-28334E5F9BDA'] 

    data['sample_list'] = []
    if settings.DYNAMIC_SAMPLE:
        for uuid in samples_bdmlID:
            try:
                root = root_model.objects.get(bdmlUUID = uuid)
                text = root.meta_data.datatype + u" in " + root.meta_data.organism + u", IDENTIFIER: " + root.meta_data.localid + "."
                limitation = 90
                if len(text) >= limitation:
                    text  = text[0:limitation] + u"..."
                
                if root.omero_datasetID and root.omero_datasetID > 0:
                    from SSBD.SSBD2.connect_omero import get_dataset_image
                    path = get_dataset_image(root.omero_datasetID, 180, 180)
                    if text and path:
                        sample_list.append((text, path, id))
            except ObjectDoesNotExist:
                pass
    else:
        data['sample_list'].append(('Nuclear division dynamics in zebrafish wild-type embryo',
                            'Keller2008.gif',
                            samples_bdmlID[0]))
        data['sample_list'].append(('Nuclear division dynamics in C. elegans wild-type embryo',
                            'Kyoda2013.gif',
                            samples_bdmlID[1]))
        data['sample_list'].append(('Single molecule dynamics in E. coli wild-type',
                            'Arjunan2010.gif',
                            samples_bdmlID[2]))
    thishost = socket.gethostname();
    if 'dhcp20' in thishost: #dhcp20
        print thishost
        # dummy
    else:
        from SSBD.SSBD2.connect_omero import get_uuid
        data['public_key'] = get_uuid()
    return render_to_response('index.html', context_instance=RequestContext(request, data))

def news(request):
    data = get_data_from_simple_form(request)
    if data['state'] == "search_success" or data['state'] == "search_fail":
        return render_to_response('search_simple2.html', context_instance=RequestContext(request, data))

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
    if filename.endswith('.zip'):
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
    data = get_data_from_simple_form(request)
    debug = ""

    try:
        #if request.user.is_anonymous() or request.user.username == settings.SSBD_ADMIN:
        #    login_user = Owner_model.objects.get(username__exact=settings.SSBD_PUBLIC)
        #else:
        #    login_user = request.user
        root = root_model.objects.get(bdmlUUID = uuid)
        data['bdml'] = root

        data['omero'] = None
        if root.omero_datasetID and root.omero_datasetID > 0:
            from SSBD.SSBD2.connect_omero import get_dataset
            data['omero'] = get_dataset(root.omero_datasetID)

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
    data = get_data_from_simple_form(request)
    if data['state'] == "search_success" or data['state'] == "search_fail":
        return render_to_response('search_simple2.html', context_instance=RequestContext(request, data))

    data['meta_id']   = id
    data['bdml_list'] = root_model.objects.filter(meta_data=id, bdml_multipart_type="1").order_by('-schema_ver') # CHECK
    return render_to_response('history2.html', context_instance=RequestContext(request, data))

class DynamicPageView(TemplateView):
    def get_template_names(self):
        return [self.kwargs['template_name']]

    def get(self, request, *args, **kwargs):
        data = get_data_from_simple_form(request)
        if data['state'] == "search_success" or data['state'] == "search_fail":
            self.template_name = 'search_simple2.html'
        return render_to_response(self.template_name, data, context_instance=RequestContext(request))

# TODO rewrite as a Object class.
def view4d(request, id):
    try:
        #if request.user.is_anonymous() or request.user.username == settings.SSBD_ADMIN:
        #    login_user = Owner_model.objects.get(username__exact=settings.SSBD_PUBLIC)
        #else:
        #    login_user = request.user
        quant = quant_data_model.objects.get(Q(pk = id)) #, Q(owner=login_user))
    except ObjectDoesNotExist:
        raise Http404()
#    minmax_t = Component_model.objects.filter(bdml_id=id).aggregate(Min('time'))
#    min_t = minmax_t['time__min']
    stats = stats_model.objects.get(bdml=quant.oldbdmlid)
    min_t = stats.min_t
    print ("SSBD2: min_t%s"% min_t)
#    context = viewer(request, id, min_t)
#    print context
    print "id = %d" % int(id)
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
        #if request.user.is_anonymous() or request.user.username == settings.SSBD_ADMIN:
        #    login_user = Owner_model.objects.get(username__exact=settings.SSBD_PUBLIC)
        #else:
        #    login_user = request.user
        quant = quant_data_model.objects.get(pk= id) #, Q(owner=login_user))
        root = root_model.objects.get(quant_data = id, schema_ver=str(0.150))
    except ObjectDoesNotExist:
        raise Http404()
#    minmax_t = Component_model.objects.filter(bdml_id=id).aggregate(Max('time'), Min('time'))
#    max_xyz = Coordinates_model.objects.filter(bdml_id=id).aggregate(

# Counting number of entitities and components directly
#    num_entities = Entity_model.objects.filter(bdml_id=id).count()
#    num_components = Component_model.objects.filter(bdml_id=id).count()
    max_xyz = stats_model.objects.get(bdml=id)
# Counting number of entitities and components using precalculated value in stats_model
    num_components = max_xyz.num_components
    num_entities = max_xyz.num_entities
    scale = ScaleUnit_model.objects.get(bdml_id=id)
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
               'bdml_id': root.quant_data.id,
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
               'tUnit':root.scaleunit.tUnit,
               'xyzUnit':root.scaleunit.xyzUnit,
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
               'tunit' : scale.tUnit,
               'scaleup' : scaleup,
               'num_components' : num_components,
               'num_entities' : num_entities
               }
    print context['name'];
    return context;

