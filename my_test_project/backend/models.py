from django.db import models
from django.contrib.gis.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField('Category name',max_length=50,help_text='Specify a cultural heritage category')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name
    
class Place(models.Model):
    categories = models.ForeignKey('Category',on_delete=models.CASCADE)
    place_name = models.CharField(max_length=50)
    description = models.TextField(max_length=254, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='place_images/', blank=True, null=True)
    active = models.BooleanField(default=True)
    point_geom = models.PointField()

    class Meta:
        verbose_name_plural = 'Places'

    def __str__(self):
        return self.place_name
    
class City(models.Model):
    name = models.CharField(max_length=50)
    point_geom = models.PointField()

    class Meta:
        verbose_name_plural = 'Cities'
    
    def __str__(self) -> str:
        return self.name