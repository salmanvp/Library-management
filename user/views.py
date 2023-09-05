from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
def register(request):
    if(request.method=="POST"):
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        s=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        s.save()
        msg="Your Register successfully"
        return render(request,"hello.html",{"msg":msg})
    return render(request, 'register.html')


def user_login(request):
    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            msg="login successfully"
            return render(request, 'hello.html', {'msg': msg})
        else:
            messages.error(request,'InvalidUser')
            msg = "User Invalid "
            return render(request,'hello.html',{'msg':msg})


    return render(request, 'login.html')


def logout(request):
    logout(request)
    return render(request, 'logout.html')
