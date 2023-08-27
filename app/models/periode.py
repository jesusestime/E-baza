from django.db import models

from app.models import Region

class Periode(models.Model):

    year = models.PositiveIntegerField(verbose_name='Année')
    region = models.ForeignKey(Region,on_delete=models.CASCADE,verbose_name='Region')
    def __str__(self):
        return str(self.year)+'('+self.region.name+'--'+self.region.indicateur.name+'--)'  