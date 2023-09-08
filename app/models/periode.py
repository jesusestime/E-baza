from django.db import models

from app.models import Sous_Region

class Periode(models.Model):

    year = models.PositiveIntegerField(verbose_name='Année')
    def __str__(self):
        return str(self.year) 