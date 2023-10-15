from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Product(models.Model):
    name = models.CharField(default="", max_length=256)
    description = models.CharField( default="", max_length=256)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    comission_value = models.DecimalField(max_digits=4, decimal_places=2)
    
    
class Seller_agent(models.Model):
    name = models.CharField( max_length=256)
    mail = models.models.DateTimeField(_(""), auto_now=True, auto_now_add=True)
    telephone = models.models.IntegerField(_(""))
    
class Client_agent(models.Model):
    name = models.CharField( max_length=256)
    mail = models.models.DateTimeField(_(""), auto_now=True, auto_now_add=True)
    telephone = models.models.IntegerField(_(""))
    
class Sale(models.Model):
    fiscal_number = models.CharField( max_length=256)
    sale_moment = models.models.DateTimeField(_(""), auto_now=True, auto_now_add=True)
    client = models.models.IntegerField(_(""))
    seller = models.models.IntegerField(_(""))
    product_list = integer_array = ArrayField(
        models.IntegerField(),
        default=list,  # You can provide a default empty list
    )
    
class WeekDays(models.Model):
    fiscal_number = models.CharField( max_length=256)
    sale_moment = models.models.DateTimeField(_(""), auto_now=True, auto_now_add=True)
    client = models.models.IntegerField(_(""))
    seller = models.models.IntegerField(_(""))
    product_list = integer_array = ArrayField(
        models.IntegerField(),
        default=list,  # You can provide a default empty list
    )