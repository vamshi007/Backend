from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Sampleserializer
from .models import SampleModel


# Create your views here.

class SampleViewset(viewsets.ModelViewSet):
    queryset = SampleModel.objects.all()
    serializer_class = Sampleserializer
