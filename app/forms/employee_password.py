from django.contrib.auth.forms import PasswordChangeForm
from app.models import Employee
from django import forms


class EmployeePasswordForm(PasswordChangeForm):
    class Meta:
        model = Employee
        fields = '__all__'