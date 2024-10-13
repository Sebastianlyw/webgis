from django.urls import path
from . import views
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [ 
    path('categories/', views.categoryList.as_view(), name=views.categoryList.name),
    path('categories/<int:pk>/', views.categoryDetail.as_view(), name=views.categoryDetail.name),
    path('places/', views.PlaceList.as_view(), name=views.PlaceList.name),
    path('places/<int:pk>/', views.PlaceDetail.as_view(), name=views.PlaceDetail.name),
    path('cities/', views.CityList.as_view(), name=views.CityList.name),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)