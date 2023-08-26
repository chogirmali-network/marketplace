from backend.apps.users.models import User
from backend.apps.core.utils.login_types import GITHUB


def get_user_by_github_login(login):
    return User.objects.filter(username=login, login_type=GITHUB, is_active=True, deleted_at__isnull=True).first()
