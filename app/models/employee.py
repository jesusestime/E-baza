from django.db import models
from django.contrib.auth.models import AbstractUser
from app.models import Employee_Service


class Employee(AbstractUser):
    SEXE = (
        ('Homme','Homme'),
        ('Femme','Femme')
    )

    PROVINCE_CHOICES = (
        ('Cankuzo', 'Cankuzo'),
        ('Gitega', 'Gitega'),
        ('Rutana', 'Rutana'),
        ('Ruyigi', 'Ruyigi'),
        ('Karuzi', 'Karuzi'),
        ('Kayanza', 'Kayanza'),
        ('Kirundo', 'Kirundo'),
        ('Muyinga', 'Muyinga'),
        ('Ngozi', 'Ngozi'),
        ('Bururi', 'Bururi'),
        ('Makamba', 'Makamba'),
        ('Rumonge', 'Rumonge'),
        ('Bubanza', 'Bubanza'),
        ('Bujumbura Mairie', 'Bujumbura Mairie'),
        ('Bujumbura Rural', 'Bujumbura Rural'),
        ('Cibitoke', 'Cibitoke'),
        ('Muramvya', 'Muramvya'),
        ('Mwaro', 'Mwaro'),
    )

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images',verbose_name='Avatar')
    registration_number = models.CharField(max_length=45,verbose_name='Numéro de matricule')
    birthday = models.DateTimeField(blank=True, null=True,verbose_name='Date de naissance') 
    sex = models.CharField(max_length=10,choices=SEXE,verbose_name='Sexe')
    tel = models.CharField(max_length=45,verbose_name='Téléphone')
    service= models.ForeignKey(Employee_Service,on_delete=models.CASCADE,verbose_name='Service employé',blank=True, null=True)
    province = models.CharField(max_length=50,choices=PROVINCE_CHOICES)

    def __str__(self):
        return self.username+"("+self.first_name +" "+self.last_name+")" 