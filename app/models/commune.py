from django.db import models
from app.models import Province

class Commune(models.Model):
    name = models.CharField(max_length=45,verbose_name='Nom')
    province = models.ForeignKey(Province,blank=True, null=True,on_delete=models.CASCADE,verbose_name='Province')
    def __str__(self):
        return  self.name+'('+self.province.name+')'  
