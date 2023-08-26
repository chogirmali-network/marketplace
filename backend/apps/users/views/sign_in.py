from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from backend.apps.users.views.users import SignInSerializer
from backend.apps.users.utils.token import sign_in_response


class SignInView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = SignInSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        return Response(sign_in_response(user), status=status.HTTP_200_OK)
