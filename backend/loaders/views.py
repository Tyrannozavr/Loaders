# views.py
from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticated
from .models import Loader
from .serializers import LoaderSerializer

class LoaderListCreateView(generics.ListCreateAPIView):
    queryset = Loader.objects.all()
    serializer_class = LoaderSerializer
    permission_classes = [IsAuthenticated]  # Require authentication

class LoaderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loader.objects.all()
    serializer_class = LoaderSerializer
    permission_classes = [IsAuthenticated]  # Require authentication

    def perform_destroy(self, instance):
        # Check if the loader has related accidents before deleting
        if instance.accidents.exists():  # Assuming 'accidents' is a related name for a ForeignKey relationship
            raise serializers.ValidationError("Cannot delete loader with associated accidents.")
        instance.delete()
