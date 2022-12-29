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
    city=models.ForeignKey(Wilaya,on_delete=models.PROTECT)
    
    

class Address(models.Model):
    street=models.CharField(max_length=255) 
    commune=models.ForeignKey(Commune,on_delete=models.PROTECT)


class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    address=models.ForeignKey(Address,on_delete=models.PROTECT)



    
	# def __str__(self):
	# 	return self.user

class Theme(models.Model):
    MATH = '0'
    PHYSIC ='1'
    BIO='2'
    TM=[
        (MATH,'mathematique'),
        (PHYSIC,'physique'),  
        (BIO,'science'),
     ]
    theme=models.CharField(
        max_length = 1 , choices = TM 
    )
class Categorie(models.Model):
    PRE = '0'
    MID ='1'
    HIGH='2'
    CAT=[
        (PRE,'Primaire'),
        (MID,'Cem'),  
        (HIGH,'Lycee'),
     ]
    categorie=models.CharField( max_length = 1 , choices = CAT)


class Annonce(models.Model):
    OFFLINE = '0'
    ONLINE ='1'
    STATE=[
        (OFFLINE,'hors ligne'),
        (ONLINE,'en ligne'),     
    ]
    
    title = models.CharField(max_length= 255)
    description = models.CharField(max_length= 1000)
    modalite=models.CharField(
        max_length = 1 , choices= STATE , default=ONLINE
    )
    tarif = models.CharField(max_length=255)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.ForeignKey(Address,on_delete=models.PROTECT)
    theme=models.ForeignKey(Theme,on_delete=models.PROTECT)
    categorie=models.ForeignKey(Categorie,on_delete=models.PROTECT)
    

class Offre(models.Model):
    comment=models.CharField(max_length=700)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    annonce=models.ForeignKey(Annonce,on_delete=models.CASCADE)
class  Favori(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    annonce=models.ForeignKey(Annonce,on_delete=models.CASCADE) 

class tof(models.Model):
    image = CloudinaryField('image')
    announce=models.ForeignKey(Annonce, on_delete=models.CASCADE)   