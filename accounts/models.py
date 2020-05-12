from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
