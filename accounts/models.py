from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True) 
    email = models.CharField(max_length=200,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ("Indoor","Indoor"),
        ('Out Door','Out Door'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True) 
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag)
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('pending','pending'),
        ('Out of Deilvery','Out of Deilvery'),
        ('Delivered','Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True , on_delete=models.SET_NULL)
    products = models.ForeignKey(Product, null=True , on_delete=models.SET_NULL)
    date_created = models.DateField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200,choices=STATUS)
    notes = models.CharField(max_length=1000,null=True)
    def __str__(self):
        return self.products.name