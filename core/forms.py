#Al igual que en Task este archivo lo hago apra separar logica y modularizar mas y mejor el codigp.

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Formualrio persnalizado para el regusrtro de usuarios
class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control'}),
        }
