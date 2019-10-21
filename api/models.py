from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField

# Create your models here.

# class Person(models.Model):
#     cpf = models.CharField(max_length=11)
#     uid = models.CharField(max_length=17)

class Location(models.Model):
    # person = models.ForeignKey(
    #         'Person',
    #         on_delete=models.CASCADE,
    #         default='1'
    #     )
    # locations = JSONField()
    cpf = models.CharField(max_length=11, null=False, default='0'),
    uid = models.CharField(max_length=17, null=False, default='0'),
    provider = models.CharField(max_length=28,  default='undefined'),
    locationProvider = models.CharField(max_length=1, null=True, default=9),
    timestamp = models.FloatField(null=False, default=0),
    latitude = models.FloatField(null=False, default=0),
    longitude = models.FloatField(null=False, default=0),
    accuracy = models.FloatField(null=True),
    speed = models.FloatField(null=True),
    altitude = models.FloatField(null=True),
    bearing = models.IntegerField(null=True)
