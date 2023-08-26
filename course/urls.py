from django.urls import path
from course import views
app_name = 'course'
urlpatterns = [
    path('' , views.course , name = 'course' ) , 
    path('category/<str:cat>' , views.course , name = 'course_cat' ) , 
]







