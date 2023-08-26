from django.shortcuts import render
from course.models import course as cr
from course.models import trainer as tr
from .models import service as service
t='trainers.html'
a='about.html'
def home(request):
    last_three_courses= cr.objects.filter(status=True)[:3]
    last_three_trainer= tr.objects.filter(status=True)[:3]
    sr = service.objects.filter(status=True)[:3]


    context ={
        'trainers' : last_three_trainer ,
        'courses' : last_three_courses ,
        'services' : sr , 
    }
    return render( request , 'root\index.html' , context=context )
def trainer(request):
    return render( request , f'root\{t}' )

def contact(request):
    return render( request , 'root\contact.html' )

def about(request):
    return render( request , f'root\{a}' )
