from dataclasses import fields

from django.forms import ModelForm

from collec_management.models import Collec, Element


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

