from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Employee_Service
from app.forms import EmployeeServiceForm

from django.contrib.auth.decorators import login_required,user_passes_test

@login_required
@user_passes_test(lambda u: u.is_superuser ,login_url="perm_is_admin")
#Display the list of the employee service
def index(request):
    assert isinstance(request, HttpRequest)
    employee_service=Employee_Service.objects.all()
    return render(
        request,
        'app/employee_services/index.html',
        {
            'employee_service':employee_service
        }
    )

@login_required
@user_passes_test(lambda u: u.is_superuser ,login_url="perm_is_admin")
#Display a form for the new employee service
def create(request):
    form = EmployeeServiceForm
    return render(
        request, 
        'app/employee_services/create.html',
        {
            'form': form
        }
    )

@login_required
@user_passes_test(lambda u: u.is_superuser ,login_url="perm_is_admin")
# Store the employee service
def store(request):
    if request.method == 'POST':
        form = EmployeeServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Le nouveau service employé a été sauvegardé avec succès ! ")
            return redirect('/employee_services')
        else:
            messages.error(request, 'Une erreur s\'est produite. Veuillez réessayer !')
            return redirect('/employee_services') 
        

@login_required
@user_passes_test(lambda u: u.is_superuser ,login_url="perm_is_admin")
# Update the employee service
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = EmployeeServiceForm()
        else:
            employee_service =Employee_Service.objects.get(pk=id)
            form = EmployeeServiceForm(instance=employee_service)
        return render(
            request,
            'app/employee_services/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = EmployeeServiceForm(request.POST)
        else:
            employee_service = Employee_Service.objects.get(pk=id)
            form = EmployeeServiceForm(request.POST,instance=employee_service)
        if form.is_valid():
            form.save()
            messages.success(request, "Le nouveau service employé a été modifiée avec succès !")
            return redirect('/employee_services')
        else:
            messages.error(request, 'Une erreur s\'est produite. Veuillez réessayer !')
            return redirect('/employee_services')


@login_required
@user_passes_test(lambda u: u.is_superuser ,login_url="perm_is_admin")
# Delete the employee service
def delete(request, id):
    employee_service = Employee_Service.objects.get(pk=id)
    employee_service.delete()
    messages.success(request, "Le service employé a été supprimé avec succès !")
    return redirect('/employee_services')