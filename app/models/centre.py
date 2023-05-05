from django.db import models
from app.models import Trimestre

class Centre(models.Model):
    name = models.CharField(max_length=255,verbose_name='Nom')
    trimestre = models.ForeignKey(Trimestre,on_delete=models.CASCADE,verbose_name='Trimestre')
    def __str__(self):
        return  self.name +'('+self.trimestre.name+'--'+self.trimestre.theme.name+'--'+self.trimestre.theme.commune.name+')' 