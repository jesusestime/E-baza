from django.db import models
class Theme(models.Model):
    name = models.CharField(max_length=255,verbose_name='Nom')
    def __str__(self):
        return  self.name