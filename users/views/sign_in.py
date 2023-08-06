from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from users.serializers.sign_in import SignInSerializer
from users.utils.auth_token import get_tokens_for_user


class SignInView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = SignInSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        return Response(get_tokens_for_user(user), status=status.HTTP_200_OK)
