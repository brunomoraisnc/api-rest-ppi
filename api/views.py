from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins

from .models import Location
from .serializers import LocationSerializer


class LocationViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    search_fields = ('cpf','latitude')
    
    def get_serializer(self, instance=None, data=None,
                    files=None, many=True, partial=False):
        return super(LocationViewSet, self).get_serializer(instance, data, files, many, partial)