from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from users.serializers.sign_up import SignUpSerializer
from users.models import User, Referral
from serializers.referral import ReferalSerializer

class SignUpView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request, referral=None):
        if referral:
            referrals = get_object_or_404(User, referral_code=referral)
            if referrals:
                    data = {
                        'invited_user': referrals.data.get('user'), 
                        'logged_in_user': request.data.get('user'),
                        'referral_code': f"{referral}"
                    }
                
                    serializer = ReferalSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({}, status=status.HTTP_201_CREATED)
