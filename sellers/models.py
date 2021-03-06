from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Seller(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    

class SellerBusiness(models.Model):
    seller = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)