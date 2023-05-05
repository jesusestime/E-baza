from django.forms import ModelForm
from app.models import Fiche
from django import forms


class FicheForm(ModelForm):
    
    class Meta:
        model = Fiche
        fields = '__all__'
