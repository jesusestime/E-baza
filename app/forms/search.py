from django import forms
from app.models import Theme,Trimestre,Commune,Centre

class ModelSearchForm(forms.Form):
    SEXE = (
        ('Homme','Homme'),
        ('Femme','Femme')
    )
    AGE =(
        ('10-14 ans','10-14 ans'),
        ('15-19 ans','15-19 ans'),
        ('20-24 ans','20-24 ans')
    )
   
    theme = forms.ModelChoiceField(queryset=Theme.objects.all(), required=False)
    commune = forms.ModelChoiceField(queryset=Commune.objects.all(), required=False)
    trimestre = forms.ModelChoiceField(queryset=Trimestre.objects.all(), required=False)
    centre = forms.ModelChoiceField(queryset=Centre.objects.all(), required=False)
    age = forms.ChoiceField(choices=AGE, required=False)
    sexe = forms.ChoiceField(choices=SEXE, required=False)