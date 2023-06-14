from rest_framework import views
from main.models import *
from rest_framework.response import Response
from .models import Wallet
from serializers.wallet import WalletSerializers
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import status

class UserCreateView(views.APIView):
    def post(self, request):
        print(request.POST)




class WalletRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get(self, request):
        wallet = get_object_or_404(Wallet, pk=request.user.id)
        serializer = WalletSerializers(wallet)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    def delete(self, request):
        Wallet.objects.filter(id=request.user.id).delete()
        return Response(data={}, status=status.HTTP_204_NO_CONTENT)

