from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=256, null=False)
    description = models.CharField(max_length=256, null=False)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    comission_value = models.DecimalField(max_digits=4, decimal_places=2, null=False)


class Seller_agent(models.Model):
    name = models.CharField(max_length=256, null=False)
    mail = models.DateTimeField(auto_now=True, null=False)
    telephone = models.CharField(max_length=256, null=False)


class Client_agent(models.Model):
    name = models.CharField(max_length=256)
    mail = models.DateTimeField(auto_now=True)
    telephone = models.CharField(max_length=256, null=False)


class Sale(models.Model):
    fiscal_number = models.CharField(max_length=256)
    sale_moment = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(Seller_agent, on_delete=models.CASCADE)
    seller = models.ForeignKey(Client_agent, on_delete=models.CASCADE)
    product_list = models.ManyToManyField(Product)
