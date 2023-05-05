from django.contrib.auth.forms import UserChangeForm
from app.models import Employee
from django import forms
import datetime


class EmployeeUpdateForm(UserChangeForm):
    class Meta:
        model = Employee
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'avatar',
            'registration_number',
            'birthday',
            'sex',
            'tel',
            'address',
            'service'
        ]

        widgets = {
            'birthday': forms.DateInput( format=('%Y-%m-%d'),attrs={'type':'date','max':datetime.date.today}),
        }