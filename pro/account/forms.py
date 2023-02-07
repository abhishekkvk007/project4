from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]

class Logform(forms.Form):
    uname=forms.CharField(max_length=100,label="Enter Username",widget=forms.TextInput(attrs={"class":"form:control"}))
    pswd=forms.CharField(max_length=100,label="Enter Password",widget=forms.PasswordInput(attrs={"class":"form:control"}))


    