from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.serializers.referrals import ReferralSerializer


class SignUpWithReferralView(APIView):
    def post(self, request, referral_code):
        serializer = ReferralSerializer(data=request.data, context={'request': request, 'referral_code': referral_code})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({}, status.HTTP_201_CREATED)
