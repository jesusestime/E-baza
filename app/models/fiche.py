from django.db import models
from app.models import Centre,Commune,Theme,Trimestre

class Fiche(models.Model):
    SEXE = (
        ('Homme','Homme'),
        ('Femme','Femme')
    )
    AGE =(
        ('10-14 ans','10-14 ans'),
        ('15-19 ans','15-19 ans'),
        ('20-24 ans','20-24 ans')
    )
    
    theme=models.ForeignKey(Theme,on_delete=models.CASCADE,verbose_name='Thème')
    commune = models.ForeignKey(Commune,on_delete=models.CASCADE,verbose_name='Commune')
    trimestre = models.ForeignKey(Trimestre,on_delete=models.CASCADE,verbose_name='Trimestre')
    centre = models.ForeignKey(Centre,on_delete=models.CASCADE,verbose_name='Centre')
    age=models.CharField(max_length=45,choices=AGE,verbose_name="Tranche d'age")
    sexe=models.CharField(max_length=45,choices=SEXE,verbose_name="Sexe")
    nombre=models.IntegerField(default=0,verbose_name="Nombre d'individus")
    institutions=models.CharField(max_length=45,verbose_name='Institutions')

    def __str__(self):
        return  self.theme.name +" "+self.commune.name+"-"+"-"+self.trimestre.name+"-"+"-"+self.centre.name+"-"+"- Entre ("+self.age+")"+self.sexe+"-"+"-"+str(self.nombre)+" individus)"  