from django.db import models
from cloudinary import CloudinaryImage
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models
from cloudinary.models import CloudinaryField


   
class Wilaya(models.Model):
    wilaya=models.CharField(max_length=100)
    
    
    
class Commune(models.Model):
    commune=models.CharField(max_length=100)
    wilaya=models.ForeignKey(Wilaya,on_delete=models.PROTECT)
    
    

class Address(models.Model):
    street=models.CharField(max_length=255) 
    commune=models.ForeignKey(Commune,on_delete=models.PROTECT)


class Utilisateur(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    address=models.ForeignKey(Address,on_delete=models.PROTECT)



    
	# def __str__(self):
	# 	return self.user

class Theme(models.Model):
    theme=models.CharField(max_length= 255)

class Categorie(models.Model):
    categorie=models.CharField(max_length= 255)


class Annonce(models.Model):
    
    
    title = models.CharField(max_length= 255)
    description = models.CharField(max_length= 1000)
    modalite=models.CharField(max_length= 255)
    tarif = models.CharField(max_length=255)
    user=models.ForeignKey(Utilisateur,on_delete=models.CASCADE)
    address=models.ForeignKey(Address,on_delete=models.PROTECT)
    theme=models.ForeignKey(Theme,on_delete=models.PROTECT)
    categorie=models.ForeignKey(Categorie,on_delete=models.PROTECT)
    date=models.DateField()
    

class Offre(models.Model):
    comment=models.CharField(max_length=700)
    user=models.ForeignKey(Utilisateur,on_delete=models.CASCADE)
    annonce=models.ForeignKey(Annonce,on_delete=models.CASCADE)
class  Favori(models.Model):
    user=models.ForeignKey(Utilisateur,on_delete=models.CASCADE)
    annonce=models.ForeignKey(Annonce,on_delete=models.CASCADE) 



class Image(models.Model):
    announce=models.ForeignKey(Annonce, on_delete=models.CASCADE) 
    image = models.ImageField('image')