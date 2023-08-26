from django.urls import path
from root import views
app_name = 'root'
urlpatterns = [
    path('' , views.home , name= 'home') ,
    path('trainer' , views.trainer , name= 'trainer' )  ,
    path('contact' , views.contact, name= 'contact' ) ,
    path('about' , views.about ,  name= 'about') ,

]