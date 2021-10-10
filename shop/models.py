from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_admin = models.BooleanField('Admin', default=False)
    is_shop = models.BooleanField('Shop', default=False)
    is_customer = models.BooleanField('Customer', default=False)

# Create your models here.
class Event(models.Model):
    image = models.ImageField(default='test.jpeg', null=True, upload_to='event/')
    name = models.CharField(max_length=255)
    date = models.DateField()
    venue = models.CharField(max_length=255)
    manager = models.CharField(max_length=255)
    description = models.TextField()

class Shop(models.Model):
    shop_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=10)
    location = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
       return self.shop_name

class Product(models.Model):
    Shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default='test.jpeg', null=True, upload_to='product/')
    product_name = models.CharField(max_length=255)
    price = models.FloatField()
    discount = models.FloatField()
    old_price = models.FloatField()


class Deal(models.Model):
    Shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default='test.jpeg', null=True, upload_to='deal/')
    deal_name = models.CharField(max_length=255)
    valid_from = models.DateField()
    valid_till = models.DateField()
    discount_percentage = models.FloatField()