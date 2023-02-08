from rest_framework import views
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import *
from django.core import serializers
from .serializers import *
import datetime

class Announce(views.APIView):
    def post(self, request):
        wilaya,created=Wilaya.objects.get_or_create(wilaya=request.data['selectedOptionWilaya'])
        commune,created=Commune.objects.get_or_create(commune=request.data['selectedOptionCommune'],wilaya=wilaya)
        address,created=Address.objects.get_or_create(commune=commune,street=request.data['street'])
        theme,created=Theme.objects.get_or_create(theme=request.data['selectedOptionTheme'])
        categorie,created=Categorie.objects.get_or_create(categorie=request.data['selectedOptionCategorie'])
        user,created =User.objects.get_or_create(username='mounia')
        user,created=Utilisateur.objects.get_or_create(user=user)
        announce, created= Annonce.objects.get_or_create(title=request.data['titre'],description=request.data['description'] ,date=datetime.date.today() ,modalite=request.data['selectedOptionModalite'],tarif=request.data['tarif'],user=user,address=address,theme=theme,categorie=categorie)
        liste=request.data['imagelink']
        for i in liste:
            image=Image(announce=announce,image=i)
            image.save()
        class_serializer=AnnonceSerializer(announce)
        return Response(class_serializer.data)
    def get(self, request):
        data =Image.objects.all()
        class_serializer=ImageSerializer(data,many=True)
        print(class_serializer.data)
        return Response(class_serializer.data)

class Home(views.APIView):
     def get(self, request):
        queryset = Image.objects.none()
        data =Annonce.objects.all()
        #theme=Theme.objects.get(theme='math')
        #data=data.filter(theme=theme)
        for a in data:
            d=Image.objects.filter(announce=a).first()
            if d is None:
                d=Image(announce=a,image=None)
                d.save()
                queryset = queryset | Image.objects.filter(announce=a)   
            else:
                 queryset = queryset | Image.objects.filter(image=d.image)        
        
        serializeddata=ImageSerializer(queryset,many=True)
        return Response(serializeddata.data)