from django import forms


class Contact_form(forms.Form):
    name = forms.CharField(max_length=1000, blank=True)
    E_mail = forms.CharField(max_length=1000, blank=True)
    phone = forms.CharField(max_length=1000, blank=True)
    URL = forms.CharField(max_length=1000, blank=True)
    organization = forms.CharField(max_length=1000, blank=True)
    department = forms.CharField(max_length=1000, blank=True)
    laboratory = forms.CharField(max_length=1000, blank=True)
    address = forms.CharField(max_length=1000, blank=True)

class Info_form(forms.Form):
    pdpmlID = forms.CharField(max_length=1000, blank=True)
    title = forms.CharField(max_length=1000, blank=True)
    version = forms.IntegerField(blank=True)
    release = forms.DateField(blank=True)

class Procedure_form(forms.Form):
    name = forms.CharField(max_length=1000, blank=True)
    order = forms.IntegerField(blank=True)
    description = forms.CharField(max_length=1000, blank=True)
    step = forms.MultipleChoiceField(Step_model.objects.all())

class Program_form(forms.Form):
    name = forms.CharField(max_length=1000, blank=True)
    version = forms.CharField(max_length=1000, blank=True)
    url = forms.CharField(max_length=1000, blank=True)
    description = forms.CharField(max_length=1000, blank=True)

class Step_form(forms.Form):
    name = forms.CharField(max_length=1000, blank=True)
    order = forms.IntegerField(blank=True)
    annotation = forms.CharField(max_length=1000, blank=True)
    program = forms.MultipleChoiceField(Program_model.objects.all())

class Summary_form(forms.Form):
    description = forms.CharField(max_length=1000, blank=True)
    contributors = forms.CharField(max_length=1000, blank=True)

class pdpmlDocument_form(forms.Form):
    version = forms.CharField(max_length=1000, blank=True)
    info = forms.MultipleChoiceField(Info_model.objects.all())
    summary = forms.MultipleChoiceField(Summary_model.objects.all())
    contact = forms.MultipleChoiceField(Contact_model.objects.all())
    procedure = forms.MultipleChoiceField(Procedure_model.objects.all())
