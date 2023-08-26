from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class SignOutView(APIView):
    def post(self, request):
        Token.objects.filter(user=request.user).delete()
        return Response({}, status.HTTP_204_NO_CONTENT)
