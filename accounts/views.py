from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import RegisterForm,LoginForm
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request,"index.html")


def signupuser(request):   
   
    form = RegisterForm(request.POST or None)    
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        
        user = authenticate(username=username, password=password)
        messages.info(request,"you are registered successfully")
        login(request, user)
        return redirect("user:login")
    
    return render(request,'register.html', {'form': form})
   


def signinuser(request):

    form = LoginForm(request.POST or None)
    context = {"form" : form}
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username,password=password)

        if user is None:
            messages.info(request,"username or password is wrong")
            return render(request,"loginuser.html",context)
        else:
            messages.success(request,"You are login successfully")
            login(request,user)
            return redirect("video:dashboard")

    return render(request,"loginuser.html",context)

def logout_user(request):
    logout(request)
    messages.info(request,"you are logout")

    return redirect("home")


