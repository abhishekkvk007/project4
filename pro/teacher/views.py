from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import AddMarkForm,StudentForm,StudentMForm
from django.contrib import messages
from .models import StudentModel
# Create your views here.
class AddMarkView(View):
    def get(self,request,*args,**kwargs):       
        f=AddMarkForm()
        return render(request,"addmark.html",{"form":f})
    def post(self,request,*args,**kwargs):
       # m1=request.POST.get("mark1")
       # m2=request.POST.get("mark2")
       # m3=request.POST.get("mark3")
       # m4=request.POST.get("mark4")
       # m5=request.POST.get("mark5")
       # mark=int(m1)+int(m2)+int(m3)+int(m4)+int(m5)
       # return render(request,"addmark.html",{"res":mark})
       form_data=AddMarkForm(data=request.POST)
       if form_data.is_valid():
             m1=form_data.cleaned_data.get("mark1")
             m2=form_data.cleaned_data.get("mark2")
             m3=form_data.cleaned_data.get("mark3")
             m4=form_data.cleaned_data.get("mark4")
             m5=form_data.cleaned_data.get("mark5") 
             mark=int(m1)+int(m2)+int(m3)+int(m4)+int(m5)
             return render(request,"addmark.html",{"res":mark})
       else:
            return render(request,"addmark.html",{"form":form_data})     

#class AddStudentView(View):
#    def get(self,request,*args,**kwargs):
#        f=StudentForm()
#        return render(request,"addstu.html",{"form":f}) 
#    def post(self,request,*args,**kwargs):
#        form_data=StudentForm(data=request.POST)
#        if form_data.is_valid():
#            fn=form_data.cleaned_data.get("first_name")
#            ln=form_data.cleaned_data.get("last_name")
#            ph=form_data.cleaned_data.get("phone")
#            age=form_data.cleaned_data.get("age")
#            email=form_data.cleaned_data.get("email")
#            addr=form_data.cleaned_data.get("address")
#            StudentModel.objects.create(first=fn,last=ln,age=age,phone=ph,email=email,address=addr)
#            messages.success(request,"Student added successfully!!")
#            return redirect("h")
#        else:
#            messages.error(request,"student adding failed!!!!")
#            return render(request,"addstu.html",{"form":form_data})    

class AddStudentMView(View):
    def get(self,request,*args,**kwargs):
        f=StudentMForm()
        return render(request,"addstu.html",{"form":f})
    def post(self,request,*args,**kwargs):
        form_data=StudentMForm(data=request.POST,files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Student added successfully!!")
            return redirect("h")
        else:
            messages.error(request,"student adding failed!!!!")
            return render(request,"addstu.html",{"form":form_data})        

class StudentListView(View):
    def get(self,request,*args,**kwargs):
        res=StudentModel.objects.all()
        return render(request,"viewstudents.html",{"data":res}) 
    
class StudDeleteView(View):
    def get(self,request,*args,**kwargs):
        sid=kwargs.get("ssid")
        stu=StudentModel.objects.get(id=sid)
        stu.delete()
        return redirect("viewstudent")    

#class StudentEditView(View):
#    def get(self,request,*args,**kwargs):
#        id=kwargs.get("sid")
#        stu=StudentModel.objects.get(id=id)
#        f=StudentForm(initial={"first_name":stu.first,"last_name":stu.last,"age":stu.age,"email":stu.email,"address":stu.address,"phone":stu.phone})
#        return render(request,"editstudent.html",{"form":f})        
#    def post(self,request,*args,**kwargs):
#        form_data=StudentForm(data=request.POST)    
#        if form_data.is_valid():
#            fn=form_data.cleaned_data.get("first_name")
#            ln=form_data.cleaned_data.get("last_name")
#            ph=form_data.cleaned_data.get("phone")
#            age=form_data.cleaned_data.get("age")
#            email=form_data.cleaned_data.get("email")
#            addr=form_data.cleaned_data.get("address")
#            id=kwargs.get("sid")
#            stu=StudentModel.objects.get(id=id)
#            stu.first=fn
#            stu.last=ln
#            stu.phone=ph
#            stu.age=age
#            stu.address=addr
#            stu.email=email
#            stu.save()
#            messages.success(request,"Student-Details Updated Successfully!!")
#            return redirect("viewstudent")
#        else:
#            messages.error(request,"Updation Failed!!")
#            return render(request,"editstudent.html",{"form":form_data})    

class StudEditMView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("sid")
        stu=StudentModel.objects.get(id=id)
        f=StudentMForm(instance=stu)
        return render(request,"editstudent.html",{"form":f})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("sid")
        stu=StudentModel.objects.get(id=id)
        form_data=StudentMForm(data=request.POST,instance=stu,files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Student-Details Updated Successfully!!")
            return redirect("viewstudent")
        else:
            messages.error(request,"Updation Failed!!")
            return render(request,"editstudent.html",{"form":form_data})        