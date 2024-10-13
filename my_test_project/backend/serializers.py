from .models import Category, Place, City
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class placeSerializer(GeoFeatureModelSerializer):
    # slugRelatedField is used to serialize a field that represents a relationship using a unique slug field on the target.
    categories = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='category_name')  
 
    class Meta:
        model = Place
        geo_field = 'point_geom'

        fields = (
            'pk',
            'categories',
            'place_name',
            'description',
            'created_at',
            'modified_at',
            'image',
        )

class citySerializer(GeoFeatureModelSerializer):
    proximity = serializers.SerializerMethodField('get_proximity')

    def get_proximity(self, obj):
        if obj.distance:
            return obj.distance.km
        return False
    
    class Meta:
        model = City
        geo_field = 'point_geom'
        fields = (
            'pk',
            'name',
            'proximity',
        )
    
