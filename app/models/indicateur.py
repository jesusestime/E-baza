from django.db import models

from app.models import Theme

class Indicateur(models.Model):

    name = models.CharField(max_length=255,verbose_name='Nom')
    theme = models.ForeignKey(Theme, null=True, on_delete=models.SET_NULL,verbose_name='Theme')
    def __str__(self):
        return  self.name