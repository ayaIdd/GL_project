
from django.contrib import admin
from django.urls import path,include,re_path
from users import views
urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('', include("mainapp.urls")),
    re_path(r'^api/users/$', views.users_list),
    re_path(r'^api/users/([0-9])$', views.users_detail),
    
]

