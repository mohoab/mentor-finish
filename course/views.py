from django.shortcuts import render
from .models import course as cr
from course.models import category as cg

def course(request):
    courses = cr.objects.filter(status=True)
    categorys = cg.objects.all()
    context = {
        'courses': courses,
        'category' : categorys,
    }
    return render( request , 'course\courses.html' , context=context )
