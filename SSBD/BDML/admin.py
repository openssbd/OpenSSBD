from django.contrib import admin
from models import \
    Component_model, \
    Contact_model, \
    Data_model, \
    Feature_model, \
    Info_model, \
    Measurement_model, \
    Methods_model, \
    Object_model, \
    Property_model, \
    ScaleUnit_model, \
    Summary_model, \
    Update_model, \
    bdmlDocument_model
#    Circle_model, \
#    Face_model, \
#    Graph_model, \
#    Line_model, \
#    Point_model, \
#    Sphere_model, \

#admin.site.register(Circle_model)
admin.site.register(Component_model)
admin.site.register(Contact_model)
admin.site.register(Data_model)
#admin.site.register(Face_model)
admin.site.register(Feature_model)
#admin.site.register(Graph_model)
admin.site.register(Info_model)
#admin.site.register(Line_model)
admin.site.register(Measurement_model)
admin.site.register(Methods_model)
admin.site.register(Object_model)
#admin.site.register(Point_model)
admin.site.register(Property_model)
admin.site.register(ScaleUnit_model)
#admin.site.register(Sphere_model)
admin.site.register(Summary_model)
admin.site.register(bdmlDocument_model)
#
admin.site.register(Update_model)

