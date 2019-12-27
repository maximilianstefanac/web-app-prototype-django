from django.contrib.gis import admin
from .models import Tree

# Register your models here.

admin.site.register(Tree, admin.OSMGeoAdmin)
