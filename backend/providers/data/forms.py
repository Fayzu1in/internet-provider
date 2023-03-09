from django import forms 
from django.contrib.auth.models import User
from .models import Callback


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'password', 
        'class': 'inpt-control', 
        'placeholder': 'Password'
    }))
    # email = forms.CharField(widget=forms.EmailInput(attrs={
    #     'class': 'inpt-control', 
    #     'placeholder': 'Email'
    # }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'inpt-control',
        'placeholder': 'Username'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')
    


class Callback(forms.ModelForm):

    class Meta:
        model = Callback
        fields = ['name',]