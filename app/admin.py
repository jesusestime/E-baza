from django.contrib import admin
from django_admin_search.admin import AdvancedSearchAdmin
from .forms import ModelSearchForm

# Register your models here.
from app.models import Region,Theme,Indicateur,Fiche,Periode,Employee,Employee_Service,Sous_Region

class MonModeleAdmin(admin.ModelAdmin):
    search_fields = ['name']


class PeriodeModeleAdmin(admin.ModelAdmin):
    search_fields = ['year']

class ModelAdmin(AdvancedSearchAdmin):
    search_form = ModelSearchForm
    search_fields = ['theme','indicateur','region','sous_region','periode', 'nombre', 'source', 'age', 'sexe']

admin.site.site_header = "E-BAZA"

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff','sex')
    
admin.site.register(Employee)
admin.site.register(Theme,MonModeleAdmin)
admin.site.register(Indicateur,MonModeleAdmin)
admin.site.register(Region,MonModeleAdmin)
admin.site.register(Fiche, ModelAdmin)
admin.site.register(Sous_Region, MonModeleAdmin)
admin.site.register(Periode,PeriodeModeleAdmin)