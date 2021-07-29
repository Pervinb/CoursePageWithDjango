"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from firstapp import views
from django.conf.urls import include

app_name = 'firstapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('blog-single/', views.blogsingle, name = "blog-single"),
    path('blog/', views.blog, name = 'blog'),
    path('contact/', views.contact, name = 'contact'),
    path('courses/', views.courses, name = 'courses'),
    path('events-single/', views.eventssingle, name = 'events-single'),
    path('events/', views.events, name = 'events'),
    path('shop-single/', views.shopsingle, name = 'shop-single'),
    path('shop/', views.shop, name = 'shop'),
    path('register/', views.register, name = 'register'),
    path('teachers/', views.teachers, name = 'teachers'),
    path('teachers-single/', views.teacherssingle, name = 'teachers-single'),
    path('courses-single/', views.coursessingle, name = 'courses-single'),
]
