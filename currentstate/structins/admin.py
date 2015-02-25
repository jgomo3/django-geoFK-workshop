from django.contrib.gis import admin
from models import Inspection, Structure

admin.site.register(Inspection, admin.GeoModelAdmin)
admin.site.register(Structure, admin.GeoModelAdmin)

