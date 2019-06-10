from django.db import models

# Create your models here.

class ApiItem(models.Model):
    cpf = models.CharField(max_length=11, default='')
    mac = models.CharField(max_length=17, default='')
    coords = models.CharField(max_length=25, default='') 
    datetime = models.DateTimeField(auto_now_add=True)
    presenca = models.CharField(max_length=1, default=0)
