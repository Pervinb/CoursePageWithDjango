from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html' )

def blogsingle(request):
    return render(request, 'blog-single.html' )

def blog(request):
    return render(request, 'blog.html' )

def contact(request):
    return render(request, 'contact.html' )

def courses(request):
    return render(request, 'courses.html' )                   


def eventssingle(request):
    return render(request, 'events-single.html' )

def events(request):
    return render(request, 'events.html' )





def register(request):
    return render(request, 'register.html')

def shopsingle(request):
    return render(request, 'shop-single.html')  

def shop(request):
    return render(request, 'shop.html')

def teacherssingle(request):
    return render(request, 'teachers-single.html')

def teachers(request):
    return render(request, 'teachers.html')    

def coursessingle(request):
    return render(request, 'courses-single.html')     