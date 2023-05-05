from django.db import models
from app.models import Theme

class Trimestre(models.Model):
    name = models.CharField(max_length=45,verbose_name='Nom')
    theme = models.ForeignKey(Theme,on_delete=models.CASCADE,verbose_name='Thème')
    def __str__(self):
        return  self.name +'('+self.theme.name+'--'+self.theme.commune.name+'--)'   