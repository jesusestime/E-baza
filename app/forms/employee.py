from django.contrib.auth.forms import UserCreationForm
from app.models import Employee
from django import forms


class EmployeeForm(UserCreationForm):

    class Meta:
        model = Employee
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        ]