from django.urls import path

from loaders.views import LoaderListCreateView, LoaderRetrieveUpdateDestroyView

urlpatterns = [
    path('/', LoaderListCreateView.as_view(), name='loader-list-create'),
    path('/<int:pk>/', LoaderRetrieveUpdateDestroyView.as_view(), name='loader-retrieve-update-destroy'),
]
