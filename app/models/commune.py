from django.db import models

class Commune(models.Model):
    name = models.CharField(max_length=45,verbose_name='Nom')
    def __str__(self):
        return  self.name