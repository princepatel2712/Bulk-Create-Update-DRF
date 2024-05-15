from rest_framework import serializers
from .models import CarModel


class CarSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = CarModel
        fields = '__all__'
