from django.urls import path
from . import views


urlpatterns = [
    path('', views.placesListMap, name ='placeslist_map'),
]