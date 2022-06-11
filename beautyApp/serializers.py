from . import models
from beautyApp.models import Services
from rest_framework import serializers


class ServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = 'id services_title services_duration services_price image'.split()


class ServicesCreateUpdateSerializer(serializers.Serializer):
    services_title = serializers.CharField(max_length=200)
    services_duration = serializers.IntegerField()
    services_price = serializers.IntegerField()
    image = serializers.ImageField()

