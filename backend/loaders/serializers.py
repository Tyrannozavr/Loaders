# serializers.py
from rest_framework import serializers
from .models import Loader

class LoaderSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='brand.name', read_only=True)
    updated_by = serializers.SerializerMethodField()

    class Meta:
        model = Loader
        fields = '__all__'

    def get_updated_by(self, obj):
        if obj.updated_by:
            return obj.updated_by.get_full_name()
        else:
            return ''


    def create(self, validated_data):
        return Loader.objects.create(**validated_data)