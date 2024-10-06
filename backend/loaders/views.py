# views.py
from rest_framework import generics, serializers, status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Loader, Brand
from .serializers import LoaderSerializer

class LoaderListCreateView(generics.ListCreateAPIView):
    queryset = Loader.objects.all()
    serializer_class = LoaderSerializer

    @permission_classes([IsAuthenticated])
    def create(self, request, *args, **kwargs):
        data = request.data
        brand = Brand.objects.get_or_create(name=data['brand'])[0]
        updated_by = request.user

        # Now use the modified data to create the object
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)  # Validate the data

        # Save the new instance
        self.perform_create(serializer)
        instance = serializer.save()
        instance.updated_by = updated_by
        instance.brand = brand
        instance.save()
        # Return the response with the created object
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoaderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loader.objects.all()
    serializer_class = LoaderSerializer
    permission_classes = [IsAuthenticated]  # Require authentication

    def perform_destroy(self, instance):
        # Check if the loader has related accidents before deleting
        if instance.accidents.exists():  # Assuming 'accidents' is a related name for a ForeignKey relationship
            raise serializers.ValidationError("Cannot delete loader with associated accidents.")
        instance.delete()
