from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    favs = models.ManyToManyRel("Annonce")


    
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
    theme=models.TextChoices(
        max_length = 1 , tm = TM 
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
    categorie=models.TextChoices(
        max_length = 1 , cat = CAT 
    )

class Comment(models.Model):
    comment=models.CharField(max_length=700)

class Annonce(models.Model):
    OFFLINE = '0'
    ONLINE ='1'
    STATE=[
        (OFFLINE,'hors ligne'),
        (ONLINE,'en ligne'),     
    ]
    
    title = models.CharField(255)
    description = models.CharField(1000)
    modalite=models.TextChoices(
        max_length = 1 , state = STATE , default=ONLINE
    )
    tarif = models.CharField(max_length=255)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    theme=models.ForeignKey(Theme,on_delete=models.PROTECT)
    categorie=models.ForeignKey(Categorie,on_delete=models.PROTECT)
    comment = models.ManyToManyRel(User,through=Comment)

class Photo(models.Model):
    url = models.CharField(max_length=255)
    announce=models.ForeignKey(Annonce, on_delete=models.CASCADE)   
    
class Wilaya(models.Model):
    wilaya=models.CharField(max_length=100)
    
    
    
class Commune(models.Model):
    commune=models.CharField(max_length=100)
    city=models.ForeignKey(Wilaya,on_delete=models.PROTECT)
    
    

class Address(models.Model):
    street=models.CharField(max_length=255) 
    commune=models.ForeignKey(Commune,on_delete=models.PROTECT)


    # CONSTANTINE='25',

    # WILAYA=[
    #     (CONSTANTINE,'CONSTANTINE'),    
    #     ] 
    
    
    # city =models.TextChoices(
    #     max_length=2, wilaya = WILAYA , default=CONSTANTINE
    # )   
    user = models.OneToOneField(User,on_delete=models.CASCADE , primary_key=False)   
    
    


