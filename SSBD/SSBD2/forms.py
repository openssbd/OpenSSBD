from django import forms


#class Circle_form(forms.Form):
#    coords = forms.CharField(max_length=1000, blank=True)
#    radius = forms.FloatField(blank=True)
#    property = forms.MultipleChoiceField(Property_model.objects.all())

class Component_form(forms.Form):
    componentID = forms.CharField(max_length=1000, blank=True)
    componentName = forms.CharField(max_length=1000, blank=True)
    time = forms.FloatField(blank=True)
    groupID = forms.CharField(max_length=1000, blank=True)
    prevID = forms.CharField(max_length=1000, blank=True)
    measurement = forms.MultipleChoiceField(Measurement_model.objects.all())

class Contact_form(forms.Form):
    name = forms.CharField(max_length=1000, blank=True)
    E_mail = forms.CharField(max_length=1000, blank=True)
    phone = forms.CharField(max_length=1000, blank=True)
    URL = forms.CharField(max_length=1000, blank=True)
    organization = forms.CharField(max_length=1000, blank=True)
    department = forms.CharField(max_length=1000, blank=True)
    laboratory = forms.CharField(max_length=1000, blank=True)
    address = forms.CharField(max_length=1000, blank=True)

class Data_form(forms.Form):
    scaleUnit = forms.MultipleChoiceField(ScaleUnit_model.objects.all())
    object = forms.MultipleChoiceField(Object_model.objects.all())
    feature = forms.MultipleChoiceField(Feature_model.objects.all())
    component = forms.MultipleChoiceField(Component_model.objects.all())

#class Face_form(forms.Form):
#    coords = forms.CharField(max_length=1000, blank=True)
#    property = forms.MultipleChoiceField(Property_model.objects.all())

class Feature_form(forms.Form):
    featureName = forms.CharField(max_length=1000, blank=True)
    featureScale = forms.FloatField(blank=True)
    featureUnit = forms.CharField(max_length=1000, blank=True)

#class Graph_form(forms.Form):
#    property = forms.MultipleChoiceField(Property_model.objects.all())

class Info_form(forms.Form):
    bdmlID = forms.CharField(max_length=1000, blank=True)
    title = forms.CharField(max_length=1000, blank=True)
    version = forms.IntegerField(blank=True)
    release = forms.DateField(blank=True)
    license = forms.CharField(max_length=1000, blank=True)

#class Line_form(forms.Form):
#    coords = forms.CharField(max_length=1000, blank=True)
#    property = forms.MultipleChoiceField(Property_model.objects.all())

class Measurement_form(forms.Form):
    objectRef = forms.CharField(max_length=1000, blank=True)
#    point = forms.MultipleChoiceField(Point_model.objects.all())
#    line = forms.MultipleChoiceField(Line_model.objects.all())
#    face = forms.MultipleChoiceField(Face_model.objects.all())
#    circle = forms.MultipleChoiceField(Circle_model.objects.all())
#    sphere = forms.MultipleChoiceField(Sphere_model.objects.all())
#    graph = forms.MultipleChoiceField(Graph_model.objects.all())

class Methods_form(forms.Form):
    summary = forms.CharField(max_length=1000, blank=True)
    source = forms.CharField(max_length=1000, blank=True)
    pdpml = forms.CharField(max_length=1000, blank=True)

class Object_form(forms.Form):
    objectName = forms.CharField(max_length=1000, blank=True)

#class Point_form(forms.Form):
#    coords = forms.CharField(max_length=1000, blank=True)
#    property = forms.MultipleChoiceField(Property_model.objects.all())

class Property_form(forms.Form):
    featureRef = forms.CharField(max_length=1000, blank=True)
    featureValue = forms.CharField(max_length=1000, blank=True)

class ScaleUnit_form(forms.Form):
    xScale = forms.FloatField(blank=True)
    yScale = forms.FloatField(blank=True)
    zScale = forms.FloatField(blank=True)
    xyzUnit = forms.CharField(max_length=1000, blank=True)
    tScale = forms.FloatField(blank=True)
    tUnit = forms.CharField(max_length=1000, blank=True)

#class Sphere_form(forms.Form):
#    coords = forms.CharField(max_length=1000, blank=True)
#    radius = forms.FloatField(blank=True)
#    property = forms.MultipleChoiceField(Property_model.objects.all())

class Summary_form(forms.Form):
    description = forms.CharField(max_length=1000, blank=True)
    organism = forms.CharField(max_length=1000, blank=True)
    datatype = forms.CharField(max_length=1000, blank=True)
    identifier = forms.CharField(max_length=1000, blank=True)
    basedon = forms.CharField(max_length=1000, blank=True)
    contributors = forms.CharField(max_length=1000, blank=True)
    citation = forms.CharField(max_length=1000, blank=True)
    PMID = forms.IntegerField(blank=True)
    dblink = forms.CharField(max_length=1000, blank=True)

class bdmlDocument_form(forms.Form):
    version = forms.CharField(max_length=1000, blank=True)
    info = forms.MultipleChoiceField(Info_model.objects.all())
    summary = forms.MultipleChoiceField(Summary_model.objects.all())
    contact = forms.MultipleChoiceField(Contact_model.objects.all())
    methods = forms.MultipleChoiceField(Methods_model.objects.all())
    data = forms.MultipleChoiceField(Data_model.objects.all())
