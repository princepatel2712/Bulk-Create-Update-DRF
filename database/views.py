from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import generics
from .serializers import CarSerializer
from .models import CarModel


class CarGenericView(generics.ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    # Method - 1 For BULK CREATE
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data, many=True)
    #     serializer.is_valid(raise_exception=True)
    #
    #     try:
    #         self.perform_create(serializer)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     except:
    #         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    # Method - 2 For BULK CREATE
    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(CarGenericView, self).get_serializer(*args, **kwargs)

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        validated_data = serializer.validated_data
        ids = [item['id'] for item in validated_data]
        instances = self.get_queryset().filter(id__in=ids)
        serializer.update(instances, validated_data)

