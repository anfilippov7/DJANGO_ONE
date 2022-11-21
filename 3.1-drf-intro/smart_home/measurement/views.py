from .models import Sensor, Measurement
from .serializers import SensorsSerializer, SensorDetailSerializer, MeasurementSerializer
from rest_framework import generics


class SensorsView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer


class MeasurementView(generics.ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorDetailView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer











