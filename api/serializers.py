from rest_framework import serializers

from .models import Location


class LocationsSerializer(serializers.Serializer):
    model = Location
    fields = '__all__'

class LocationSerializer(serializers.Serializer):
    
    class Meta:
        locations = LocationsSerializer(many=True)
        # model = Location
        # fields = '__all__'
