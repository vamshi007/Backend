from .models import SampleModel
from rest_framework import serializers


class Sampleserializer(serializers.ModelSerializer):
    class Meta:
        model = SampleModel
        fields = "__all__"
