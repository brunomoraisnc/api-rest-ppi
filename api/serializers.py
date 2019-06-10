from rest_framework import serializers

from .models import ApiItem


class ApiItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApiItem
        fields = '__all__'
