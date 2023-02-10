from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UploadForm(ModelForm):
    class Meta:
        model=Uploadedimg
        fields='__all__'

class UserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2')
    def seve(self,commit=True):
        user=super(UserCreationForm,self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.seve()
        return user