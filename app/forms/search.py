from django import forms
from app.models import Periode

class ModelSearchForm(forms.Form):
    SEXE = (
        ('Homme','Homme'),
        ('Femme','Femme'),
        ('Non défini','Non défini'),
    )

    AGE =(
        ('10-14 ans','10-14 ans'),
        ('15-19 ans','15-19 ans'),
        ('20-24 ans','20-24 ans'),
        ('25-49 ans','25-49 ans'),
    )
   
    periode = forms.ModelChoiceField(queryset=Periode.objects.all(), required=False)
    age = forms.ChoiceField(choices=AGE, required=False)
    sexe = forms.ChoiceField(choices=SEXE, required=False)