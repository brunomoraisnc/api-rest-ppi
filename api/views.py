from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import ApiItem
from .serializers import ApiItemSerializer


class ApiItemViewSet(viewsets.ModelViewSet):

    serializer_class = ApiItemSerializer
    queryset = ApiItem.objects.all()