from django.db import models
from django.core.exceptions import ValidationError

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
    # cpf = models.CharField(max_length=11, null=False, default='0')
    # uid = models.CharField(max_length=17, null=False, default='0')
    # provider = models.CharField(max_length=28,  default='undefined')
    # locationProvider = models.CharField(max_length=1, null=True, default=9)
    # timestamp = models.FloatField(null=False, default=0)
    # latitude = models.FloatField(null=False, default=0)
    # longitude = models.FloatField(null=False, default=0)
    # accuracy = models.FloatField(null=True)
    # speed = models.FloatField(null=True)
    # altitude = models.FloatField(null=True)
    # bearing = models.IntegerField(null=True)
    # isFromMockProvider = models.CharField(null=True, max_length=20)
    # mockLocationsEnabled = models.CharField(null=True, max_length=20)
    cpf = models.CharField(max_length=200, null=False, default='0')
    uid = models.CharField(max_length=200, null=False, default='0')
    provider = models.CharField(max_length=200, null=False, default='0')
    locationProvider = models.CharField(max_length=200, null=False, default='0')
    timestamp = models.CharField(max_length=200, null=False, default='0')
    latitude = models.CharField(max_length=200, null=False, default='0')
    longitude = models.CharField(max_length=200, null=False, default='0')
    accuracy = models.CharField(max_length=200, null=False, default='0')
    speed = models.CharField(max_length=200, null=True, default='0')
    altitude = models.CharField(max_length=200, null=False, default='0')
    bearing = models.CharField(max_length=200, null=True, default='0')
    isFromMockProvider = models.CharField(max_length=200, null=False, default='0')
    mockLocationsEnabled = models.CharField(max_length=200, null=False, default='0')