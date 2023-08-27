from django.contrib.auth.forms import UserCreationForm
from app.models import Employee
from django import forms
import datetime


class EmployeeForm(UserCreationForm):

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
            'province'
        ]
        widgets = {
            'birthday': forms.DateInput( format=('%Y-%m-%d'),attrs={'type':'date','max':datetime.date.today}),
        }