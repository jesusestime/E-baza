from django.db import models
from app.models import Periode,Theme,Indicateur,Region,Sous_Region

class Fiche(models.Model):
    SEXE = (
        ('Homme','Homme'),
        ('Femme','Femme'),
        ('Non défini','Non défini'),
    )


    theme = models.ForeignKey(Theme,on_delete=models.CASCADE,verbose_name='Thème')
    indicateur = models.ForeignKey(Indicateur,on_delete=models.CASCADE,verbose_name='Indicateur')
    region=models.ForeignKey(Region,on_delete=models.CASCADE,verbose_name='Région')
    sous_region=models.ForeignKey(Sous_Region,on_delete=models.CASCADE,verbose_name='Sous région')
    periode = models.ForeignKey(Periode,on_delete=models.CASCADE,verbose_name='Période')
    age=models.CharField(max_length=45,verbose_name="Tranche d'age")
    sexe=models.CharField(max_length=45,choices=SEXE,verbose_name="Sexe",null=True)
    nombre=models.CharField(max_length=45,verbose_name="Nombre d'individus",null=True)
    source=models.CharField(max_length=45,verbose_name='Source')

    def __str__(self):
        return  self.theme.name+'--'+self.indicateur.name+'--'+self.region.name+'--'+self.sous_region.name+'--'+str(self.periode.year) +"- Age ("+self.age+")"+self.sexe+"-"+"-"+str(self.nombre)+" individus)"+"-------"+str(self.source)