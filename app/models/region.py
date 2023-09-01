from django.db import models

from app.models import Indicateur

class Region(models.Model):

    name = models.CharField(max_length=255,verbose_name='Nom')
    indicateur = models.ForeignKey(Indicateur,on_delete=models.CASCADE,verbose_name='Indicateur')
    
    def __str__(self):
        return  self.name+'('+self.indicateur.name+'--'+self.indicateur.theme.name+')'  