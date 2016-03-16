from django.contrib import admin
from models import \
    Contact_model, \
    Info_model, \
    Procedure_model, \
    Program_model, \
    Step_model, \
    Summary_model, \
    pdpmlDocument_model

admin.site.register(Contact_model)
admin.site.register(Info_model)
admin.site.register(Procedure_model)
admin.site.register(Program_model)
admin.site.register(Step_model)
admin.site.register(Summary_model)
admin.site.register(pdpmlDocument_model)

