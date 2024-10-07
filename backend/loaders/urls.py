from django.urls import path

from loaders.views import LoaderListCreateView, LoaderRetrieveUpdateDestroyView, IncidentListCreateView

urlpatterns = [
    path('/', LoaderListCreateView.as_view(), name='loader-list-create'),
    path('/<int:pk>/', LoaderRetrieveUpdateDestroyView.as_view(), name='loader-retrieve-update-destroy'),
    path('/incidents/', IncidentListCreateView.as_view(), name='incident-list-create'),
]
