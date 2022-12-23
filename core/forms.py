from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User 
from .models import *
from datetime import date, datetime
from django.contrib.admin import widgets  
 
class MyUser(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Passoword'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
        }

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
    )

class Showdate(forms.ModelForm):
    date = forms.DateField(initial=date.today, widget=forms.SelectDateWidget(attrs={'type': 'date','class':'form-control'}))
    class Meta:
        model = Userdate
        fields = ['date']

class Shownote(forms.ModelForm):
    time = forms.TimeField(initial= datetime.now(), widget=forms.TimeInput(attrs = {'class':'form-control'}))
    task= forms.CharField(widget = forms.widgets.Textarea(attrs={'class':'form-control','rows':3,'placeholder':'Enter your task'}))
    class Meta:
        model = Usernote
        fields = ['time','task']