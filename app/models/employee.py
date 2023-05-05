from django.db import models
from django.contrib.auth.models import AbstractUser
from app.models import Employee_Service


class Employee(AbstractUser):
    SEXE = (
        ('Homme','Homme'),
        ('Femme','Femme')
    )

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images',verbose_name='Avatar')
    registration_number = models.CharField(max_length=45,verbose_name='Numéro de matricule')
    birthday = models.DateTimeField(blank=True, null=True,verbose_name='Date de naissance') 
    sex = models.CharField(max_length=10,choices=SEXE,verbose_name='Sexe')
    tel = models.CharField(max_length=45,verbose_name='Téléphone')
    address = models.CharField(max_length=45,verbose_name='Adresse')
    service= models.ForeignKey(Employee_Service,on_delete=models.CASCADE,verbose_name='Service employé',blank=True, null=True)
    

    def __str__(self):
        return self.username+"("+self.first_name +" "+self.last_name+")" 