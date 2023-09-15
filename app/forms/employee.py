from django.contrib.auth.forms import UserCreationForm
from app.models import Employee
from django import forms
import datetime


class EmployeeForm(UserCreationForm):
    accept_terms = forms.BooleanField(
        label='Accepter nos termes et conditions',
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'text-dark'})
    )

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
            'service',
            'sex',
            'accept_terms',  # Add the 'accept_terms' field to the form
        ]
        widgets = {
            'birthday': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date', 'max': datetime.date.today}),
        }