from django.utils import timezone
from django.utils.translation import gettext as _
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token


class CustomTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        token = Token.objects.filter(key=key, created__gte=timezone.now() - timezone.timedelta(days=1)).first()

        if token is None:
            Token.objects.filter(key=key).delete()
            raise AuthenticationFailed({'detail': _('Invalid or expired token.'), 'logout': 'true'})

        if not token.user.is_active:
            raise AuthenticationFailed({'detail': _('User inactive or deleted.'), 'logout': 'true'})

        return token.user, token
