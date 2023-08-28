from django.db.models import Sum
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from app.models import  Theme,Indicateur,Region,Periode,Fiche,Employee
from django.contrib.auth.decorators import login_required,user_passes_test


@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser ,login_url="perm_is_employee")
def theme(request):
    themes = Theme.objects.all()
    return render(request, 'app/home/themes.html', {'themes':themes})


def navbar(request):
    themes = Theme.objects.all()
    indicateurs = Indicateur.objects.all()
    return {'themes': themes, 'indicateurs': indicateurs}


@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser ,login_url="perm_is_employee")
def indicateur(request, theme_id):
    theme = get_object_or_404(Theme, pk=theme_id)
    indicateurs = theme.indicateur_set.all()
    return render(request, 'app/home/indicateurs.html', {'theme': theme, 'indicateurs': indicateurs})

@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser ,login_url="perm_is_employee")
def region(request,theme_id, indicateur_id):
    indicateur = get_object_or_404(Indicateur, pk=indicateur_id)
    theme = get_object_or_404(Theme, pk=theme_id)
    regions = indicateur.region_set.all()
    return render(request, 'app/home/regions.html', { 'theme': theme, 'indicateur': indicateur,'regions':regions})


@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser ,login_url="perm_is_employee")
def periode(request,theme_id, indicateur_id,region_id):
    indicateur = get_object_or_404(Indicateur, pk=indicateur_id)
    theme = get_object_or_404(Theme, pk=theme_id)
    region = get_object_or_404(Region, pk=region_id)
    periodes = region.periode_set.all()
    return render(request, 'app/home/periodes.html', {'theme': theme, 'indicateur': indicateur,'region':region,'periodes':periodes})

@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser ,login_url="perm_is_employee")
def fiche(request,theme_id, indicateur_id,region_id,periode_id):
    indicateur = get_object_or_404(Indicateur, pk=indicateur_id)
    theme = get_object_or_404(Theme, pk=theme_id)
    region = get_object_or_404(Region, pk=region_id)
    periode = get_object_or_404(Periode, pk=periode_id)
    fiches = Fiche.objects.filter(periode=periode)
    total = fiches.aggregate(Sum('nombre'))
    return render(request, 'app/home/fiches.html', {'theme': theme, 'indicateur': indicateur,'region':region,'periode':periode, 'total': total,'fiches': fiches})


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


@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser ,login_url="perm_is_employee")
def index(request):
    indicateur = Indicateur.objects.count()
    theme = Theme.objects.count()
    region = Region.objects.count()
    user =  Employee.objects.count()
    return render(request, 'app/home/index.html', {'theme': theme, 'indicateur': indicateur,'region':region,'user':user})


# @login_required
# @user_passes_test(lambda u: u.is_staff or u.is_superuser ,login_url="perm_is_employee")
# def all_themes(request):
#     themes = Theme.objects.all()
#     return render(request, 'app/home/all_themes.html', {'themes': themes})
