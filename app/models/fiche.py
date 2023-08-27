from django.db import models
from app.models import Periode

class Fiche(models.Model):
    SEXE = (
        ('Homme','Homme'),
        ('Femme','Femme'),
        ('Non défini','Non défini'),
    )

    AGE =(
        ('10-14 ans','10-14 ans'),
        ('15-19 ans','15-19 ans'),
        ('20-24 ans','20-24 ans'),
        ('25-49 ans','25-49 ans'),
    )
    periode = models.ForeignKey(Periode,on_delete=models.CASCADE,verbose_name='Période')
    age=models.CharField(max_length=45,choices=AGE,verbose_name="Tranche d'age")
    sexe=models.CharField(max_length=45,choices=SEXE,verbose_name="Sexe")
    nombre=models.IntegerField(default=0,verbose_name="Nombre d'individus")
    source=models.CharField(max_length=45,verbose_name='Source')

    def __str__(self):
        return  str(self.periode.year) +"- Age ("+self.age+")"+self.sexe+"-"+"-"+str(self.nombre)+" individus)"+"-------"+str(self.source)