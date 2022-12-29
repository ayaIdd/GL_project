from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Annonce_2(models.Model):
    title = models.CharField(255)
    description = models.CharField(1000)
    tarif = models.CharField(max_length=255)
   
    
    