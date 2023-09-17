from django.contrib.auth.forms import UserCreationForm
from app.models import Employee
from django import forms
import datetime
from django.utils.safestring import mark_safe
from django.urls import reverse_lazy


class EmployeeForm(UserCreationForm):
    accept_terms = forms.BooleanField(required=True, widget=forms.CheckboxInput(attrs={'class': 'text-dark'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['accept_terms'].label = mark_safe('Accepter <a href="{}">nos termes et conditions</a>'.format(reverse_lazy('terms')))

    class Meta:
        model = Employee
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
            'birthday',
            'tel',
            'province',
            'proffesion',
            'domaine',
            'sex',
            'accept_terms',  # Add the 'accept_terms' field to the form
        ]
        widgets = {
            'birthday': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date', 'max': datetime.date.today}),
        }