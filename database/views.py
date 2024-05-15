from rest_framework.response import Response
from rest_framework.viewsets import generics
from rest_framework import status
from .models import CarModel
from .serializers import CarSerializer


class CreateCarView(generics.ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def create(self, request, *args, **kwargs):
        if not isinstance(request.data, list):
            return Response({"error": "Expected a list of items"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        CarModel.objects.bulk_create([CarModel(**item) for item in serializer.validated_data])
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=self.get_success_headers(serializer.data))


class UpdateCarView(generics.RetrieveUpdateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        if not isinstance(request.data, list):
            return Response({"error": "Expected a list of items"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        ids = [item['id'] for item in serializer.validated_data]
        cars_to_update = CarModel.objects.filter(id__in=ids)
        cars_dict = {car.id: car for car in cars_to_update}
        fields_to_update = set()
        for item in serializer.validated_data:
            car = cars_dict.get(item['id'])
            if car:
                for field, value in item.items():
                    if field != 'id':
                        setattr(car, field, value)
                        fields_to_update.add(field)
        if fields_to_update:
            CarModel.objects.bulk_update(cars_to_update, fields_to_update)
        return Response(serializer.data, status=status.HTTP_200_OK)
