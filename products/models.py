from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    name     = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.TextField()
    nutrition = models.ForeignKey('Nutrition', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

class Image(models.Model):
    image_url = models.CharField(max_length=500)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

class Nutrition(models.Model):
    one_serving_kca = models.FloatField()
    sodium_mg = models.FloatField()
    saturated_fat_g = models.FloatField()
    sugars_g = models.FloatField()
    protein_g = models.FloatField()
    caffeine_mg = models.FloatField()
    size_ml = models.CharField(max_length=20)
    size_fluid_ounce = models.CharField(max_length=20)

    class Meta:
        db_table = 'nutritions'

class Allergy(models.Model):
    name = models.CharField(max_length=20)
    bridge = models.ManyToManyField(Product, through='Allergy_product')

    class Meta:
        db_table = 'allergies'

class Allergy_product(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergy_products'
