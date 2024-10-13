from .models import Place, Category,City
from .serializers import categorySerializer, placeSerializer, citySerializer
from rest_framework import generics

from django.http import Http404
from django.contrib.gis.db.models.functions import Distance 
from django.shortcuts import get_object_or_404

class categoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = categorySerializer
    name = 'category-list'

class categoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = categorySerializer
    name = 'category-detail'

class PlaceList(generics.ListCreateAPIView):
    queryset = Place.objects.filter(active=True)
    serializer_class = placeSerializer
    name = 'place-list'

class PlaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Place.objects.filter(active=True)
    serializer_class = placeSerializer
    name = 'place-detail'

class CityList(generics.ListAPIView):
    serializer_class = citySerializer
    name = 'cities-list'
    def get_queryset(self):
        placeID = self.request.query_params.get('placeid')
        if placeID is None:
            return Http404
        
        selectedPlaceGeom = get_object_or_404(Place, pk=placeID).point_geom
        return City.objects.annotate(distance=Distance('point_geom', selectedPlaceGeom)).order_by('distance')[:3]