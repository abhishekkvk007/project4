from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import RegForm,Logform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
class HomeView(View):
    def get(self,request,*args,**kwargs):
        us=request.user
        return render(request,"main_home.html",{"user":us})

class RegView(View):
    def get(self,request,*args,**kwargs):
        f=RegForm()
        return render(request,"reg.html",{"form":f}) 
    def post(self,request,*args,**kwargs):
        form_data=RegForm(data=request.POST)   
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"User registered successfully")
            return redirect("log")
        else:
            messages.error(request,"Registration failed")
            return render(request,"reg.html",{"form":form_data})    

class LogView(View):
    def get(self,request,*args,**kwargs):
       f=Logform()
       return render(request,"login.html",{"form":f})
    def post(self,request,*args,**kwargs):
        form_data=Logform(data=request.POST)
        if form_data.is_valid():
            un=form_data.cleaned_data.get("uname")
            ps=form_data.cleaned_data.get("pswd")
            user=authenticate(request,username=un,password=ps)  
            if user:
                login(request,user)
                messages.success(request,"Login Successful")
                return redirect("h")
            else:
                messages.error(request,"Login Failed")
                return redirect("log")
        else:
            return render(request,"login.html",{"form":form_data})

class LogoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("log")


