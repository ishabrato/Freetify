from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . models import MyUser

class MyRegFrm(UserCreationForm):
    username=forms.CharField(label="Username",
            widget=forms.TextInput(attrs={'class':'form-control border-primary','placeholder':'Enter Username'}))
    first_name=forms.CharField(label="First Name",
            widget=forms.TextInput(attrs={'class':'form-control border-primary','placeholder':'Enter First name'}))
    last_name=forms.CharField(label="Last Name",
            widget=forms.TextInput(attrs={'class':'form-control border-primary','placeholder':'Enter Last name'}))
    email=forms.CharField(label="Email-ID",
            widget=forms.EmailInput(attrs={'class':'form-control border-primary','placeholder':'Enter Email ID'}))
    password1=forms.CharField(label="Password",
            widget=forms.PasswordInput(attrs={'class':'form-control border-primary','placeholder':'Enter password'}))
    password2=forms.CharField(label="Confirm Password",
            widget=forms.PasswordInput(attrs={'class':'form-control border-primary','placeholder':'Confirm password'}))
    class Meta:
        model = MyUser
        fields = ("username", 'first_name', 'last_name', 'email')

class LoginFrm(AuthenticationForm):
    username=forms.CharField(label="Username",
            widget=forms.TextInput(attrs={'class':'form-control border-primary','placeholder':'Enter Username'}))
    password=forms.CharField(label="Password",
            widget=forms.PasswordInput(attrs={'class':'form-control border-primary','placeholder':'Enter password'}))