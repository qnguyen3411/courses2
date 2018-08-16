from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from .models import *
# Create your views here.
def index(request):
    data = {
        'courses' : Course.objects.all()
    }
    return render(request, "coursesApp/index.html", data)

def delete_page(request, id):
    #check if id is a valid id
    match = Course.objects.filter(id=id)
    if match:
        data={ 'course' : match[0] }
        return render(request, "coursesApp/delete_page.html",data)

    else:
        return redirect('/')

def course_page(request,id):
    match = Course.objects.filter(id=id)
    if match:
        data={ 'course' : match[0] }
        return render(request, "coursesApp/course_page.html",data)

    else:
        return redirect('/')

def add_process(request):
    if request.method == 'POST':
        errors = Course.objects.length_validator(request.POST)
        if len(errors):
            for key,value in errors.items():
                messages.error(request, value, extra_tags='comment') 
                print(messages.error)
        else:
            this_course = Course.objects.create(name=request.POST['name'])
            Description.objects.create(content=request.POST['description'], course=this_course)
       
    return redirect('/')

def delete_process(request,id):
    match = Course.objects.filter(id=id)
    if match:
        match[0].delete()
        print("YEY")
        return redirect('/')
    else:
        return redirect('/')

def add_comment(request, id):
    #check if we arrived here via POST
    if request.method == "POST":
    #check if post information is valid
        errors = Comment.objects.length_validator(request.POST)
        #if there are errors
        if len(errors):
            for key,value in errors.items():
                messages.error(request, value, extra_tags='comment') 
                print(messages.error)
        else:
            match = Course.objects.filter(id=id)
            if match:
                Comment.objects.create(content=request.POST['comment'], course=match[0])
                return redirect('/show/'+str(id))
    return redirect('/')