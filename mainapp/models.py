from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()
#settings.Auth_user_Mode
#************
# 1.Category
# 2.Product
# 3.CartProduct
# 4.Cart
# 5.Order
#************
# 6.Customer
# 7.Specification



#/category/lego(slug!!!)/
class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Nazwa Kategorii')
    #унікальний
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Products(models.Model):

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Kategoria', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Nazwa producta')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Image')
    description = models.TextField(verbose_name='Opis', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Cena')

    def __str__(self):
        return self.title


class LegoZestawy(Products):

    type_product = models.CharField(max_length=255, verbose_name='Typ productu')
    Marka = models.CharField(max_length=255, verbose_name='Marka productu')
    Age = models.CharField(max_length=255, verbose_name='Przedział wiekowy')
    Material = models.CharField(max_length=255, verbose_name='Material productu')

    def __str__(self):
        return "{}: {}".format(self.category.name,self.title)

class LegoFigure(Products):
    type_product = models.CharField(max_length=255, verbose_name='Typ productu')
    Marka = models.CharField(max_length=255, verbose_name='Marka productu')
    Age = models.CharField(max_length=255, verbose_name='Przedział wiekowy')
    Material = models.CharField(max_length=255, verbose_name='Material productu')

    def __str__(self):
        return "{}: {}".format(self.category.name,self.title)

class CartProduct(models.Model):

    user = models.ForeignKey('Customer', verbose_name='Klient', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Koszyk', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')
    quentety = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Koncowa cena')

    def __str__(self):
        return 'Product: {} (dla koszyka)'.format(self.product.title)

class Cart(models.Model):

    owner = models.ForeignKey('Customer', verbose_name='Kto zrobil', on_delete=models.CASCADE)
    product = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Koncowa cena')

    def __str__(self):
        return str(self.id)



class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name='korzystać', on_delete=models.CASCADE)
    phone = models.CharField(max_length=28, verbose_name='Numer telefonu')
    addres = models.CharField(max_length=255, verbose_name='Adres')

    def __str__(self):
        return 'Klient: {} {}'.format(self.user.first_name, self.last_name)

# class Specification(models.Model):
#
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     name = models.CharField(max_length=255, verbose_name='Opis dla towarów')
#
#     def __str__(self):
#         return 'Opis dla towarów: {}'.format(self.name)
