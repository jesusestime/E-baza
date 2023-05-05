from django.contrib import admin
from django_admin_search.admin import AdvancedSearchAdmin
from .forms import ModelSearchForm

# Register your models here.
from app.models import Centre,Commune,Employee_Service,Employee,Fiche,Theme,Trimestre

class MonModeleAdmin(admin.ModelAdmin):
    search_fields = ['name']

class ModelAdmin(AdvancedSearchAdmin):
    search_form = ModelSearchForm
    search_fields = ['theme', 'commune', 'trimestre', 'centre', 'age', 'sexe']

admin.site.site_header = "E-BAZA"

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff','sex')
    
admin.site.register(Employee)
admin.site.register(Centre,MonModeleAdmin)
admin.site.register(Commune,MonModeleAdmin)
admin.site.register(Employee_Service,MonModeleAdmin)
admin.site.register(Fiche, ModelAdmin)
admin.site.register(Theme,MonModeleAdmin)
admin.site.register(Trimestre,MonModeleAdmin)