from django.db import models
from django.contrib.auth.models import User

class Admin(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Annonce_2(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    tarif = models.CharField(max_length=255)
   
    
    