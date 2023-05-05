from django.db import models
from app.models import Commune
class Theme(models.Model):
    name = models.CharField(max_length=255,verbose_name='Nom')
    commune = models.ForeignKey(Commune,on_delete=models.CASCADE,verbose_name='Commune')
    def __str__(self):
        return  self.name+'('+self.commune.name+')'  