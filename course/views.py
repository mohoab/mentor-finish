from django.shortcuts import render
from .models import course as cr
from course.models import category as cg
from django.core.paginator import Paginator
from django.core.paginator import  PageNotAnInteger , EmptyPage
def course(request,cat=None,trainer=None,cname=None):
    c = cg.objects.all()
    
    if cat :
       courses = cr.objects.filter(category__title=cat ) 
    elif cname :
       courses = cr.objects.filter(category__title=cname ) 
    elif trainer :
        courses = cr.objects.filter(trainer__info__username=trainer)
    elif request.GET.get('search') :
        courses = cr.objects.filter(content__contains=request.GET.get('search'))
    else:
        courses = cr.objects.filter(status=True)
    courses = Paginator(courses,3)
    first_page = 1
    last_page= courses.num_pages
    try :
        page_number =request.GET.get('page')
        courses = courses.get_page(page_number)
    
    except EmptyPage:
        courses = courses.get_page(1)
    except PageNotAnInteger :
        courses = courses.get_page(last_page)

    context={
        'courses': courses,
        'category' : c,
        'first' : first_page ,
        'last' :last_page ,
    }
    return render( request , 'course\courses.html' , context=context )


def course_detail(request , id ) :
    id_list = []
    course=cr.objects.filter(status=True)
    for c in course:
        id_list.append(c)
    id_list.reverse()

    try:
        course_detail = cr.objects.filter(id=id)
        if id==0 :
            per_course = None
            next_course = cr.objects.get(id=id_list[1])
        elif id==id_list[-1]:
            next_course = None
            per_course = cr.objects.get(id=id_list[-2])
        else:
            next_course = cr.object.get(id=id_list[id_list.index(id)+1])
            per_course = cr.object.get(id=id_list[id_list.index(id)-1])

        context = {
            'cd': course_detail ,
            'next_course': next_course , 
            'per_course': per_course , 
        }

        return render( request , 'course/course-details.html' , context=context )
    except :
        return render( request , 'course/404.html' )