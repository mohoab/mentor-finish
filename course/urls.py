from django.urls import path
from course import views
app_name = 'course'
urlpatterns = [
    path('' , views.course , name = 'course' ) , 
    path('category/<str:cat>' , views.course , name = 'course_cat' ) , 
    path('trainer/<str:trainer>' , views.course , name = 'course_trainer' ) , 
    path('category/<str:cname>' , views.course , name = 'course_cname' ) , 
    path('search/' , views.course , name = 'course_search' ) ,
    path('<int:id>' , views.course_detail , name = 'course_datail' ) ,
]







