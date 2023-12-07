from django.db import models

from app.models import Region

class Sous_Region(models.Model):

    name = models.CharField(max_length=255,verbose_name='Nom')
    region = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL,verbose_name='Région')
    
    def __str__(self):
        return  self.name  