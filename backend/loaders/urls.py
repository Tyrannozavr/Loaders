from django.urls import path

from loaders.views import LoaderListCreateView, LoaderRetrieveUpdateDestroyView, IncidentListCreateView, \
    IncidentRetrieveUpdateDestroyView, search_loaders

urlpatterns = [
    path('/', LoaderListCreateView.as_view(), name='loader-list-create'),
    path('/search/', search_loaders, name='loader-search'),
    path('/<int:pk>/', LoaderRetrieveUpdateDestroyView.as_view(), name='loader-retrieve-update-destroy'),
    path('/incidents/', IncidentListCreateView.as_view(), name='incident-list-create'),
    path('/incidents/<int:pk>/', IncidentRetrieveUpdateDestroyView.as_view(),)
]
