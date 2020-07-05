from django.db import models

# Create your models here.
class CommonPlace(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Country(CommonPlace):
    code = models.CharField(max_length=3)

class Province(CommonPlace):
    code = models.CharField(max_length=3)
    country = models.ForeignKey(Country, models.PROTECT)

class Departament(CommonPlace):
    province = models.ForeignKey(Province, models.PROTECT)

class Place(CommonPlace):
    departament = models.ForeignKey(Departament, models.PROTECT)

class Category(models.Model):
    name = models.CharField(max_length=50)

class Shop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    instagram = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photo',blank=True,null=True,verbose_name='Photo')
    category = models.ForeignKey(Category, models.PROTECT)
    place = models.ForeignKey(Place, models.PROTECT)
    created_at = models.DateTimeField('')