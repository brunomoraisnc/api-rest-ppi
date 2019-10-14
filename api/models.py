from django.db import models

# Create your models here.

class Location(models.Model):
    cpf = models.CharField(max_length=11)
    uid = models.CharField(max_length=17)
    coords = models.CharField(max_length=25)
    date = models.DateTimeField(auto_now_add=True)
    datetime = models.DateTimeField(auto_now_add=True)
    presenca = models.CharField(max_length=1)
