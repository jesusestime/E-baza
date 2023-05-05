from django.db import models

class Employee_Service(models.Model):
    status = models.CharField(max_length=45)
    name = models.CharField(max_length=45,default="Non spécifié",verbose_name='Nom')
    def __str__(self):
        return  self.name +"( "+self.status+" )"