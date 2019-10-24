from rest_framework import serializers

from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    model = Location
    fields = '__all__'

class LocationsSerializer(serializers.Serializer):
    
    class Meta:
        locations = LocationSerializer(many=True)
        # model = Location
        # fields = '__all__'
