from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins

from .models import Location
from .serializers import LocationSerializer


class LocationViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    search_fields = ('cpf','latitude')
    
    def post(self, request, *args, **kwargs):
        urls = request.data

        is_many = isinstance(urls, list)
        if not is_many:
            return super(LocationViewSet, self).create(request, *args, **kwargs)
        else:
            serializer = self.get_serializer(data=urls, many=True)
            serializer.is_valid(raise_exception=True)
            self.create_list(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def create(self, request, *args, **kwargs):
    #     """
    #     #checks if post request data is an array initializes serializer with many=True
    #     else executes default CreateModelMixin.create function 
    #     """
    #     is_many = isinstance(request.data, list)
    #     if not is_many:
    #         return super(LocationViewSet, self).create(request, *args, **kwargs)
    #     else:
    #         serializer = self.get_serializer(data=request.data, many=True)
    #         serializer.is_valid(raise_exception=True)
    #         self.perform_create(serializer)
    #         headers = self.get_success_headers(serializer.data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)