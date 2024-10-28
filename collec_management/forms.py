from django import forms
from .models import Collec

class CollecForm(forms.ModelForm):
    class Meta:
        model = Collec
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }