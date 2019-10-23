from rest_framework import serializers

from .models import Location


class LocationsSerializer(serializers.ListSerializer):
    model = Location
    fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    
    class Meta:
        locations = LocationsSerializer(many=True)
        # model = Location
        # fields = '__all__'
