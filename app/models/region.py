from django.db import models

from app.models import Indicateur

class Region(models.Model):

    name = models.CharField(max_length=255,verbose_name='Nom')
    
    def __str__(self):
        return  self.name