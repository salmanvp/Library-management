"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from .import views
app_name="book"

urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add,name='addbook'),
    path('views',views.view,name='viewbook'),
    path('hello',views.views,name='views'),
    path('hey',views.addstudent,name='view student'),
    path('fact',views.fact,name='fact'),
    path('addbook1',views.addbook1,name='addbook1'),
    path('addstudent1',views.addstudent1,name='addstudent1'),
    path('nextview/<int:p>/',views.nextview,name='nextview'),
    path('delete/<int:p>/',views.delete,name='delete'),
    path('edit/<int:p>/',views.edit,name='edit')

]
