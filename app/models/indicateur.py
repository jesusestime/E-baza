from django.db import models

from app.models import Theme

class Indicateur(models.Model):

    name = models.CharField(max_length=255,verbose_name='Nom')
    theme = models.ForeignKey(Theme,on_delete=models.CASCADE,verbose_name='Theme')
    def __str__(self):
        return  self.name