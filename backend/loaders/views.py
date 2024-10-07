# views.py
from rest_framework import generics, serializers, status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

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


class LoaderRetrieveUpdateDestroyView(APIView):
    queryset = Loader.objects.all()
    serializer_class = LoaderSerializer
    permission_classes = [IsAuthenticated]  # Require authentication

    def put(self, request, pk):
        loader = self.get_object(pk)  # Assuming you have a method to get the loader instance
        request.data['brand'] = Brand.objects.get_or_create(name=request.data.get('brand'))[0]
        request.data['updated_by'] = request.user
        serializer = LoaderSerializer(loader, data=request.data, partial=False)

        if serializer.is_valid():
            # Accessing the validated data
            brand = Brand.objects.get_or_create(name=request.data.get('brand'))[0]
            user = request.user

            # Save the serializer if needed
            instance = serializer.save()
            instance.updated_by = user
            instance.brand = brand
            instance.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        # Your logic to get the loader object by primary key (pk)
        return Loader.objects.get(pk=pk)
