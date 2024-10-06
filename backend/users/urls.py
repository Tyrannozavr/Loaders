from django.urls import path

from users.views import UserRegistrationView, CustomAuthToken

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='register'),  #
    path('login/', CustomAuthToken.as_view(), name='token'),  #
]