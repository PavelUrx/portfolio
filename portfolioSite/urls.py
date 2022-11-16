from django.contrib import admin
from django.urls import path  
from . import views  
      
    
urlpatterns = [  
    path('pageadmin/', admin.site.urls),  
    path('', views.index, name='index'),
    ]  

