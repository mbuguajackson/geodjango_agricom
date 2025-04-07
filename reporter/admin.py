from django.contrib import admin
from . models import Incidence, Counties
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
class IncidenceAdmin(LeafletGeoAdmin):
    pass
    #list_display=('name','location')

class CountiesAdmin(LeafletGeoAdmin):
    #pass
    list_display=('county','area')
admin.site.register(Incidence, IncidenceAdmin)
admin.site.register(Counties, CountiesAdmin)