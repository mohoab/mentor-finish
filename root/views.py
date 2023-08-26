from django.shortcuts import render
from course.models import course as cr
from course.models import trainer as tr
from course.models import category as cg
from django.contrib.auth.models import User as us
from .models import service as service

t='trainers.html'
a='about.html'
def home(request):
    user_count = us.objects.all().count()
    course_count = cr.objects.filter(status=True).count()
    trainer_count = tr.objects.filter(status=True).count()
    service_count = service.objects.filter(status=True).count()
    last_three_courses= cr.objects.filter(status=True)[:3]
    last_three_trainer= tr.objects.filter(status=True)[:3]
    sr = service.objects.filter(status=True)[:3]
    categorys = cg.objects.all()


    context ={
        'trainers' : last_three_trainer ,
        'courses' : last_three_courses ,
        'services' : sr , 
        'category': categorys ,
        'uc' : user_count , 
        'cc' : course_count , 
        'tc' : trainer_count , 
        'sc' : service_count ,
    }
    return render( request , 'root\index.html' , context=context )
def trainer(request):
    categorys = cg.objects.all()
    context = {
        'category' : categorys
    }
    return render( request , f'root\{t}' ,context=context)

def contact(request):
    categorys = cg.objects.all()
    context = {
        'category' : categorys ,
    }
    return render( request , 'root\contact.html' ,context=context )

def about(request):
    categorys = cg.objects.all()
    context = {
        'category' : categorys
    }
    return render( request , f'root\{a}' , context=context)
