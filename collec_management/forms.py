from dataclasses import fields

from django.forms import ModelForm

from collec_management.models import Collec, Element

from django.contrib.auth.models import User

from django import forms


class CollecForm(ModelForm) :
    class Meta :
        model = Collec
        fields = ["title","description"]
        labels = {
            "title": "Titre",
            "description": "Description"
        }

class ElementForm(ModelForm) :
    class Meta :
        model = Element
        fields = ["title","description","value","quantity","collec"]
        labels = {
            "title": "Titre",
            "description": "Description",
            "value": "Valeur",
            "quantity": "Quantité",
            "collec": "Collection"
        }

class loginForm(forms.Form) :
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'}),
        label="Nom d'utilisateur",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}),
        label="Mot de passe",
    )
class registerForm(forms.ModelForm) :
    class Meta :
        model = User
        fields = ["email","username","password"]
        labels = {
            "email": "Email",
            "username": "Nom d'utilisateur",
            "password": "Mot de passe"
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre email'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre mot de passe'}),
        }
