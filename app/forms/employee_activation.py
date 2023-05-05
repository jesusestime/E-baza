from django.contrib.auth.forms import UserChangeForm
from app.models import Employee
from django import forms


class EmployeeActivateForm(UserChangeForm):
    class Meta:
        model = Employee
        fields = [
            'is_superuser',
            'is_staff'
        ]