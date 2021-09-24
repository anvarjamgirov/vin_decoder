from rest_framework import serializers
from api import models


class VINDecodeRequestSerializer(serializers.Serializer):
    vin_code = serializers.CharField(required=True, help_text="VIN number")

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class VINDecodeResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.VIN
        fields = ('vin_code', 'make', 'model', 'year', 'manufacturer', 'engine', 'trim', 'transmission')
