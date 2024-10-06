# serializers.py
from rest_framework import serializers
from .models import Loader

class LoaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loader
        fields = '__all__'
