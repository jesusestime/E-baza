from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Fiche
from app.forms import FicheForm
from django.contrib.auth.decorators import login_required,user_passes_test

@login_required
@user_passes_test(lambda u: u.is_superuser ,login_url="perm_is_admin")
#Display the list of the fiche
def index(request):
    assert isinstance(request, HttpRequest)
    fiche=Fiche.objects.all()
    return render(
        request,
        'app/fiches/index.html',
        {
            'fiche':fiche
        }
    )


@login_required
@user_passes_test(lambda u: u.is_superuser ,login_url="perm_is_admin")
# Display a form for 
def create(request):
    form = FicheForm
    return render(
        request, 
        'app/fiches/create.html',
        {
            'form': form
        }
    )





@login_required
@user_passes_test(lambda u: u.is_superuser ,login_url="perm_is_admin")
# Store the the 
def store(request):
    if request.method == 'POST':
        form = FicheForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Le nouveau fiche a été sauvegardé avec succès ! ")
            return redirect('/fiches')
        else:
            messages.error(request, 'Une erreur s\'est produite. Veuillez réessayer !')
            return redirect('/fiches') 



@login_required
@user_passes_test(lambda u: u.is_superuser ,login_url="perm_is_admin")
# Update the 
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = FicheForm()
        else:
            fiche =Fiche.objects.get(pk=id)
            form = FicheForm(instance=fiche)
        return render(
            request,
            'app/fiches/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = FicheForm(request.POST)
        else:
            Fiche = Fiche.objects.get(pk=id)
            form = FicheForm(request.POST,instance=Fiche)
        if form.is_valid():
            form.save()
            messages.success(request, "Le nouveau fiche a été modifiée avec succès !")
            return redirect('/fiches')
        else:
            messages.error(request, 'Une erreur s\'est produite. Veuillez réessayer !')
            return redirect('/fiches')

@login_required
@user_passes_test(lambda u: u.is_superuser ,login_url="perm_is_admin")
# Delete the 
def delete(request, id):
    fiche = Fiche.objects.get(pk=id)
    fiche.delete()
    messages.success(request, "Le fiche a été supprimé avec succès !")
    return redirect('/fiches')