from django.shortcuts import render
from .models import course as cr
from course.models import category as cg

def course(request,cat=None):
    c = cg.objects.all()
    if cat :
       courses = cr.objects.filter(category__title=cat ) 
    else:
        courses = cr.objects.filter(status=True)
    
    context = {
        'courses': courses,
        'category' : c,
    }
    return render( request , 'course\courses.html' , context=context )
