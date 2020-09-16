from django.shortcuts import render,redirect
from .forms import Signup,LoginF
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.
def signup(request):
    form=Signup(request.POST or None)
    if form.is_valid():
        username= form.cleaned_data.get("username")
        password= form.cleaned_data.get("password")
        newUser= User(username=username)
        newUser.set_password(password)
        newUser.save() 

        login(request,newUser)
        messages.success(request,"You've signed up succesfully")
        return redirect("index")
    else:
        form= Signup()
        context={"form":form}
        return render(request,"signup.html",context)

def loginn(request):
    form=LoginF(request.POST or None)
    context={"form":form}
    if form.is_valid():
        username= form.cleaned_data.get("username")
        password= form.cleaned_data.get("password")

        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"Error")
            return render(request,"login.html",context)
        else:
            messages.success(request,"Logged in succesfully")
            login(request,user)
            return redirect("index")
    else:
        return render(request,"login.html",context)

def logoutt(request):
    logout(request)
    messages.success(request,"Logged out")
    return redirect("index")