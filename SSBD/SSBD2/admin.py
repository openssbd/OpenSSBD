from django.contrib import admin
#from models import \
#    Component_model, \
#    Feature_model, \
#    Measurement_model, \
#    Methods_model, \
#    Object_model, \
#    Property_model, \
#    ScaleUnit_model, \

#admin.site.register(Point_model)
#admin.site.register(Sphere_model)
# admin.site.register(Update_model)

from django.contrib.auth.admin import UserAdmin
from django.conf import settings

from SSBD.SSBD2.models import *
from SSBD.SSBD2.bdmlweb_forms import OwnerChangeForm, OwnerCreationForm

class News_admin(admin.ModelAdmin):
    list_display = ("date", "title", "text")

class Owner_admin(UserAdmin):
    form = OwnerChangeForm
    add_form = OwnerCreationForm

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active')
    list_filter = ('email',) 
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'is_active')}),
        ('Important dates', {'fields': ('last_login','date_joined')}),
        ('Additional info', {'fields': ('phone','URL','organization','department','laboratory','address')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name',)}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

class Link_database_admin(admin.ModelAdmin):
    list_display = ("meta_data", "database", "URL","symbol", "category", "organism", "gene")

admin.site.register(News_model, News_admin)
admin.site.register(Owner_model, Owner_admin)
admin.site.register(link_database_model, Link_database_admin)

admin.site.register(root_model)
admin.site.register(bdml_multipart_model)
admin.site.register(meta_data_model)
admin.site.register(quant_data_model)

