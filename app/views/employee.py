from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import os

from django.contrib.auth.decorators import login_required,user_passes_test

from app.models import Employee

from django.contrib.auth import update_session_auth_hash

from app.forms import EmployeeForm,EmployeeUpdateForm,EmployeeActivateForm,EmployeePasswordForm

@login_required
@user_passes_test(lambda u: u.is_superuser ,login_url="perm_is_admin")
# Display employees
def index(request):
    employee = Employee.objects.all()
    return render(
        request,
        'app/employees/index.html',
        {
            'employee': employee
        }
    )

# Show employee register form
def register(request):
    form =EmployeeForm()
    return render(
        request, 
        'app/employees/register.html',
        {
            'form': form
        }
    )

# Login form
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        Employee = authenticate(request, username=username, password=password)
        if Employee is not None:
            login(request, Employee)
            return redirect('/')
        else:
            messages.info(request, 'L\'identifiant ou le mot de passe est incorrect')
            
    return render(
        request,
        'app/employees/login.html'
    )


# Register a new employee    
def store(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else: 
            messages.error(request, 'Veuillez corriger l(es)\'erreur (s)ci-dessous.')
            return redirect('/register')
        
@login_required 
# Logout an authenticated employee
def user_logout(request):
    logout(request)
    messages.info(request, 'Déconnexion réussie de l\'utilisateur')
    return redirect('/login')

@login_required
# Get employee profile
def user_view(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET" or "POST":
        if id == 0:
            employee=request.user
        else:
            employee =Employee.objects.get(pk=id)
        return render(
            request,
            'app/employees/view.html',
            {
                'employee': employee
            }
        )
    

@login_required
# Edit existing employee
def user_edit(request,id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = EmployeeUpdateForm()
        else:
            employee =Employee.objects.get(pk=id)
            form = EmployeeUpdateForm(instance=employee)
        return render(
            request,
            'app/employees/edit.html',
            {
                'form': form,
                'id':id
            }
        )
    else:
        if id == 0:
            form = EmployeeUpdateForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeUpdateForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            if request.FILES.get('avatar', None) != None:
                try:
                    os.remove(request.user.avatar.url)
                except Exception as e:
                    print('Exception in removing old profile image: ', e)
                request.user.avatar = request.FILES['avatar']
                request.user.save()
            messages.success(request, "L'utilisateur a été mis à jour avec succès !")
            return redirect('employee_view', id=request.user.id)
        else:
            messages.error(request, 'Veuillez corriger l(es)\'erreur(s)ci-dessous.')
            return redirect('employee_edit', id=request.user.id)


@login_required
@user_passes_test(lambda u: u.is_superuser ,login_url="perm_is_admin")
#Delete the existing employee
def user_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    messages.success(request, "L'utilisateur a été supprimé avec succès !")
    return redirect('/employees')


@login_required
@user_passes_test(lambda u: u.is_superuser ,login_url="perm_is_admin")
# Activate an existing employee
def user_activation(request,id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = EmployeeActivateForm
        else:
            employee =Employee.objects.get(pk=id)
            form = EmployeeActivateForm(instance=employee)
        return render(
            request,
            'app/employees/activate.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = EmployeeActivateForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeActivateForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        messages.success(request, "Le statut de l'utilisateur  été mis à jour avec succès !")
        return redirect('/employees')
    

@login_required
# Change password for existing employee
def user_password(request,id):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = EmployeePasswordForm(request.user, request.POST)
        if form.is_valid():
            employee=Employee
            employee = form.save()
            update_session_auth_hash(request, employee)
            messages.success(request, 'Votre mot de passe a été mis à jour avec succès!')
            return redirect('employee_login')
        else:
            messages.error(request, "Veuillez corriger l(es)'erreur(s)ci-dessous.")
    else:
        form = EmployeePasswordForm(request.user)
    return render(request, 'app/employees/password_change.html', {
        'form': form
    })
