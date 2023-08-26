from django.shortcuts import render
from .models import course as cr

def course(request):
    courses = cr.objects.filter(status=True)
    context = {
        'courses': courses
    }
    return render( request , 'course\courses.html' , context=context )
