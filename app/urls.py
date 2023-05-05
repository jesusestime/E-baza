from django.urls import path
from app.views import employee_service,employee,home


urlpatterns = [

   

   path('employee_services/', employee_service.index, name='employee_service_index'),
   path('employee_services/create', employee_service.create, name='employee_service_create'),
   path('employee_services/store', employee_service.store, name='employee_service_store'),
   path('employee_services/edit/<int:id>', employee_service.edit, name='employee_service_edit'),
   path('employee_services/delete/<int:id>', employee_service.delete,name='employee_service_delete'),
              

   path('employees/', employee.index, name='employee_index'),
   path('login/', employee.user_login, name='employee_login'),
   path('register/', employee.register, name='employee_register'),
   path('employees/store', employee.store, name='employee_store'),
   path('logout/', employee.user_logout, name='employee_logout'),
   path('employees/view/<int:id>', employee.user_view, name='employee_view'),
   path('employees/edit/<int:id>', employee.user_edit, name='employee_edit'),
   path('employees/delete/<int:id>', employee.user_delete, name='employee_delete'),
   path('employees/activate/<int:id>', employee.user_activation, name='employee_activate'),
   path('employees/password/<int:id>', employee.user_password, name='employee_password'),
        


   path('perm/employee/', home.perm_is_employee, name='perm_is_employee'),
   path('perm/admin/', home.perm_is_admin, name='perm_is_admin'),

    path('', home.index, name='index'),
    path('themes/<int:commune_id>/', home.themes, name='themes'),
    path('trimestres/<int:commune_id>/<int:theme_id>/', home.trimestres, name='trimestres'),
    path('centres/<int:commune_id>/<int:theme_id>/<int:trimestre_id>/', home.centres, name='centres'),
    path('fiche/<int:commune_id>/<int:theme_id>/<int:trimestre_id>/<int:centre_id>/', home.fiche, name='fiche'),
 
]

