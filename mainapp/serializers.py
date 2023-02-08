from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class WilayaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wilaya
        fields =  '__all__'

class CommuneSerializer(serializers.ModelSerializer):
    wilaya = WilayaSerializer(read_only=True)
    class Meta:
        model = Commune
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    commune = CommuneSerializer(read_only=True)
    class Meta:
        model = Address
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UtilisateurSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    address = AddressSerializer(read_only=True)
    class Meta:
        model = Utilisateur
        fields = '__all__'
 
class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class AnnonceSerializer(serializers.ModelSerializer):
    theme = ThemeSerializer(read_only=True)
    Categorie = CategorieSerializer(read_only=True)
    address = AddressSerializer(read_only=True)
    user = UtilisateurSerializer(read_only=True)
    class Meta:
        model = Annonce
        fields = '__all__'

class OffreSerializer(serializers.ModelSerializer):
    user = UtilisateurSerializer(read_only=True)
    annonce = AnnonceSerializer(read_only=True)
    class Meta:
        model = Offre
        fields = '__all__'

class FavoriSerializer(serializers.ModelSerializer):
    user = UtilisateurSerializer(read_only=True)
    annonce = AnnonceSerializer(read_only=True)
    class Meta:
        model = Favori
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    announce = AnnonceSerializer(read_only=True)
    class Meta:
        model =Image
        fields = '__all__'