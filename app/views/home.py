from django.db.models import Sum
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from app.models import  Commune, Theme, Trimestre, Centre, Fiche
from django.contrib.auth.decorators import login_required,user_passes_test

@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser ,login_url="perm_is_employee")
def index(request):
    communes = Commune.objects.all()
    return render(request, 'app/home/index.html', {'communes': communes})

@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser ,login_url="perm_is_employee")
def themes(request, commune_id):
    commune = get_object_or_404(Commune, pk=commune_id)
    themes = commune.theme_set.all()
    return render(request, 'app/home/themes.html', {'commune': commune, 'themes': themes})

@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser ,login_url="perm_is_employee")
def trimestres(request,commune_id, theme_id):
    commune = get_object_or_404(Commune, pk=commune_id)
    theme = get_object_or_404(Theme, pk=theme_id)
    trimestres = theme.trimestre_set.all()
    return render(request, 'app/home/trimestres.html', { 'commune': commune, 'theme': theme, 'trimestres': trimestres})

@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser ,login_url="perm_is_employee")
def centres(request,  commune_id, theme_id, trimestre_id):
    commune = get_object_or_404(Commune, pk=commune_id)
    theme = get_object_or_404(Theme, pk=theme_id)
    trimestre = get_object_or_404(Trimestre, pk=trimestre_id)
    centres = trimestre.centre_set.all()
    return render(request, 'app/home/centres.html', {'commune': commune, 'theme': theme, 'trimestre': trimestre, 'centres': centres})

@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser ,login_url="perm_is_employee")
def fiche(request,commune_id, theme_id, trimestre_id, centre_id):
    commune = get_object_or_404(Commune, pk=commune_id)
    theme = get_object_or_404(Theme, pk=theme_id)
    trimestre = get_object_or_404(Trimestre, pk=trimestre_id)
    centre = get_object_or_404(Centre, pk=centre_id)
    fiches = Fiche.objects.filter(commune=commune, theme=theme, trimestre=trimestre, centre=centre)
    total = fiches.aggregate(Sum('nombre'))
    return render(request, 'app/home/fiche.html', {'commune': commune, 'theme': theme, 'trimestre': trimestre, 'centre': centre, 'fiches': fiches, 'total': total})


# Display a view for after redirecting the new employee without is_staff or is_superuser roles
def perm_is_employee(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/perm/employee.html'
    )

# Display a view for after redirecting the employee without is_superuser role
def perm_is_admin(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/perm/admin.html'
    )