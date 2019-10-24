from rest_framework import serializers

from .models import Location


class LocationsSerializer(serializers.ModelSerializer):
    model = Location
    fields = '__all__'

class LocationSerializer(serializers.Serializer):
    locations = LocationsSerializer(many=True)
    # class Meta:
        
        # model = Location
        # fields = '__all__'
