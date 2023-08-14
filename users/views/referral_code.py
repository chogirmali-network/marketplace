from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from users.models import Referral



class ReferralCodeAPI(APIView):
    def post(self, request, referrer):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            
            main_referrer = Referral.objects.filter().first()
            if main_referrer:
                Referral.objects.create(user=User, referrer=main_referrer)
            return Response({'detail': 'Login successful.'}, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED) 