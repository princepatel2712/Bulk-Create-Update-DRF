from rest_framework import serializers
from .models import CarModel


class BulkUpdateCarSerializer(serializers.ListSerializer):
    def update(self, instances, validated_data):
        instance_mapping = {instance.id: instance for instance in instances}
        result = []
        for data in validated_data:
            instance = instance_mapping.get(data['id'])
            if instance is not None:
                result.append(self.child.update(instance, data))
        return result


class CarSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = CarModel
        fields = '__all__'
        list_serializer_class = BulkUpdateCarSerializer

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
