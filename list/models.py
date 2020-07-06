from django.db import models

# Create your models here.
class CommonPlace(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        abstract = True

class Country(CommonPlace):
    code = models.CharField(max_length=3)
    class Meta:
        verbose_name_plural = "countries"

class Province(CommonPlace):
    code = models.CharField(max_length=3)
    country = models.ForeignKey(Country, models.PROTECT)

class Departament(CommonPlace):
    province = models.ForeignKey(Province, models.PROTECT)

class Place(CommonPlace):
    departament = models.ForeignKey(Departament, models.PROTECT)

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200,blank=True,null=True,)
    phone = models.CharField(max_length=20,blank=True,null=True,)
    whatsapp = models.CharField(max_length=20,blank=True,null=True,)
    instagram = models.CharField(max_length=50,blank=True,null=True,)
    image = models.ImageField(upload_to='media',blank=True,null=True,verbose_name='Photo')
    category = models.ForeignKey(Category, models.PROTECT)
    place = models.ForeignKey(Place, models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name