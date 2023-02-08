from django.urls import path,re_path
from .views import *
from users import views

urlpatterns = [
    path('post/', Announce.as_view(), name='post'),
    path('get/', Announce.as_view(), name='get'),
    path('home/', Home.as_view(), name='get'),
   
]