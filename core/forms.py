from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import User





class SingUpForm(UserChangeForm):
    first_name=forms.CharField(max_length=50,required=True)
    last_name=forms.CharField(max_length=50,required=True)
    email=forms.CharField(max_length=50,required=True)

    
    class Meta:
        fields = ['username','first_name','last_name','password1','password2']
