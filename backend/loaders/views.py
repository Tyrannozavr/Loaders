# views.py
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Brand, Incidents
from .models import Loader  # Assuming your Loader model is in the same app
from .serializers import LoaderSerializer, IncidentSerializer


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

    def get_object(self, pk):
        # Your logic to get the loader object by primary key (pk)
        return Loader.objects.get(pk=pk)

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

    def delete(self, request, pk):
        loader = self.get_object(pk)
        if loader.incidents.exists():
            return Response({'reason': 'incidents'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            loader.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['GET'])
@permission_classes([AllowAny])
def search_loaders(request):
    queryset = Loader.objects.all()

    # Get the search term from query parameters
    search_term = request.GET.get('number', None)

    if search_term:
        # Filter loaders by number, case insensitive
        queryset = queryset.filter(number__icontains=search_term)

    # Serialize the queryset
    loaders_data = [{'id': loader.id, 'number': loader.number} for loader in queryset]

    return Response(loaders_data, status=status.HTTP_200_OK)


class IncidentListCreateView(generics.ListCreateAPIView):
    queryset = Incidents.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = IncidentSerializer

    def get_queryset(self):
        loader_id = self.request.query_params.get('loaderId', None)
        if loader_id:
            return Incidents.objects.filter(loader_id=loader_id)
        else:
            return Incidents.objects.all()


class IncidentRetrieveUpdateDestroyView(APIView):
    queryset = Incidents.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return Incidents.objects.get(pk=pk)

    def put(self, request, pk):
        incident = self.get_object(pk)  # Assuming you have a method to get the loader instance
        serializer = IncidentSerializer(incident, data=request.data, partial=False)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        incident = self.get_object(pk)
        incident.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



