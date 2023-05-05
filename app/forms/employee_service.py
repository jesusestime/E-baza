from django.forms import ModelForm
from app.models import Employee_Service
from django import forms

class EmployeeServiceForm(ModelForm):
    
    class Meta:
        model = Employee_Service
        fields = '__all__'