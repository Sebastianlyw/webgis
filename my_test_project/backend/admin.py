from django.contrib.gis import admin

from .models import Category, Place, City

# Register your models here.
admin.site.register(Category)

class CustomGeoAdmin(admin.GISModelAdmin):
    gis_widget_kwargs ={
        'attrs': {
            'default_zoom': 5,
            'default_lon': 174.886,
            'default_lat': -40.9006,
        }
    }
    # openlayers_url = 'https://openlayers.org/api/2.13/OpenLayers.js'
    # extra_js = ['https://openlayers.org/api/2.13/OpenLayers.js']

@admin.register(Place)
class PlaceAdmin(CustomGeoAdmin):
    pass
    # list_display = ('place_name','categories','active')
    # list_filter = ('categories','active')
    # search_fields = ('place_name','description')
    # ordering = ('place_name',)

@admin.register(City)
class CityAdmin(CustomGeoAdmin):
    pass