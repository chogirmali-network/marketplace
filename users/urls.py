from django.urls import path
from users.views import UserCreateView, WalletRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-create'),
    path("wallet/", WalletRetrieveUpdateDestroyAPIView.as_view(), name="wallet_destroy_retrieve"),
]

