from django import forms
from .models import StudentModel

class AddMarkForm(forms.Form):
    mark1=forms.IntegerField(label="Enter Mark of Subject1")
    mark2=forms.IntegerField(label="Enter Mark of Subject2")
    mark3=forms.IntegerField(label="Enter Mark of Subject3")
    mark4=forms.IntegerField(label="Enter Mark of Subject4")
    mark5=forms.IntegerField(label="Enter Mark of Subject5")
    def clean(self):
        cleaned_data=super().clean()
        m1=cleaned_data.get("mark1")
        m2=cleaned_data.get("mark2")
        if m1<0:
            msg="MArk less than zero.Invalid Input"
            self.add_error("mark1",msg)
        if m2<0:
            msg="MArk less than zero.Invalid Input"
            self.add_error("mark2",msg)



class StudentForm(forms.Form):
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your first name"}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your last name"}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter your age"}))
    address=forms.CharField(max_length=500,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your address"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter your email"}))
    phone=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter your phone number"})) 
    def clean(self):
        cleaned_data=super().clean()
        fn=cleaned_data.get("first_name")
        ln=cleaned_data.get("last_name")
        age=cleaned_data.get("age")
        ph=str(cleaned_data.get("phone"))

        if fn==ln:
            self.add_error("last_name","Firstname and lastname are same") 
        if age<1:
            self.add_error("age","Age is invalid")
        if len(ph)!=10:
            self.add_error("phone","Digits are not 10")    

class StudentMForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields="__all__"      
        widgets={
            "first":forms.TextInput(attrs={"class":"form-control","placeholder":"First Name"}),
            "last":forms.TextInput(attrs={"class":"form-control","placeholder":"Last Name"}),
            "age":forms.NumberInput(attrs={"class":"form-control","placeholder":"Age"}),
            "address":forms.Textarea(attrs={"class":"form-control","placeholder":"Address"}),
            "phone":forms.NumberInput(attrs={"class":"form-control","placeholder":"Phone Number"}),
            "email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Email ID"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),
        }      
    def clean(self):
        cleaned_data=super().clean()
        fn=cleaned_data.get("first")
        ln=cleaned_data.get("last")
        age=cleaned_data.get("age")
        ph=str(cleaned_data.get("phone"))

        if fn==ln: 
            self.add_error("last","Firstname and lastname are same") 
        if age<1:
            self.add_error("age","Age is invalid")
        if len(ph)!=10:
            self.add_error("phone","Digits are not 10")        