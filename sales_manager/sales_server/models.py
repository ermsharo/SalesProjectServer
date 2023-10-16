from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(default="", max_length=256)
    description = models.CharField(default="", max_length=256)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    comission_value = models.DecimalField(max_digits=4, decimal_places=2)


class Seller_agent(models.Model):
    name = models.CharField(max_length=256)
    mail = models.DateTimeField(auto_now=True)
    telephone = models.IntegerField(default="")


class Client_agent(models.Model):
    name = models.CharField(max_length=256)
    mail = models.DateTimeField(auto_now=True)
    telephone = models.IntegerField(default="")


class Sale(models.Model):
    fiscal_number = models.CharField(max_length=256)
    sale_moment = models.DateTimeField(auto_now=True)
    client = models.IntegerField()
    seller = models.IntegerField()
    product_list =  ArrayField(
        models.IntegerField(),
        default=list,
    )
