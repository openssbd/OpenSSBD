from __future__ import unicode_literals
from django.forms.formsets import formset_factory
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, ReadOnlyPasswordHashField
from models import Owner_model

MODE_CHOICES = (
    ('AND', 'AND'),
    ('OR', 'OR'),
    ('NOT', 'NOT'),
)

#    ('status',       'status',       'root_model'),
BDML_FIELD_CHOICES = (
    ('all_fields',   'All Fields',   'all'),
    ('bdmlUUID',     'bdmlID',       'root_model'),
    ('schema_ver',   'schema',       'root_model'),
    ('title',        'title',        'meta_data'),
    ('description',  'description',  'meta_data'),
    ('organism',     'organism',     'meta_data'),
    ('datatype',     'datatype',     'meta_data'),
    ('localid',      'localID',      'meta_data'),
    ('basedon',      'basedon',      'meta_data'),
    ('contributors', 'contributors', 'meta_data'),
    ('PMID',         'PMID',         'meta_data'),
    ('name',         'contactname',  'meta_data'),
    ('organization', 'organization', 'meta_data'),
)

class SearchForm(forms.Form):
    F = zip(*[ zip (*BDML_FIELD_CHOICES)[0], zip(*BDML_FIELD_CHOICES)[1]])
    conf  = forms.CharField(required=False, max_length=3, widget=forms.Select(choices=MODE_CHOICES))
    field = forms.CharField(required=False, max_length=100, widget=forms.Select(choices=F))
    value = forms.CharField(required=False, max_length=200)

SearchFormSet = formset_factory(SearchForm, extra=1, max_num=10, can_delete=False)

class OwnerCreationForm(forms.ModelForm):
    oldpassword = forms.CharField(label='Password', widget=forms.PasswordInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model=Owner_model
        fields = ('username', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(OwnerCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class OwnerChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model=Owner_model

    def clean_password(self):
        return self.initial["password"]

class OwnerProfileForm(forms.ModelForm):
    class Meta:
        model = Owner_model
        exclude = ('username', 'password', 'is_active', 'date_joined', 'last_login',)

    def __init__(self, *args, **kwargs):
        super(OwnerProfileForm, self).__init__(*args, **kwargs)
