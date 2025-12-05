from django import forms   #for importing forms
from django.contrib.auth.models import User   #for importing user with which we are working
from django.contrib.auth.forms import UserCreationForm     #for importing user creation form
from .models import Profile
from urllib import request

class UserRegistration(UserCreationForm):
    first_name = forms.CharField(max_length=25)     #first_name variable is used because it is by the same name in the database
    last_name = forms.CharField(max_length=25)      #last_name variable name is user because it is by the same name in the database
    email = forms.EmailField()                      #for taking input in email form

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']