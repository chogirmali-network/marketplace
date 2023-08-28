from users.models import User
from core.utils.login_types import GITHUB


def get_user_by_github_login(login):
    return User.objects.filter(username=login, login_type=GITHUB, is_active=True, deleted_at__isnull=True).first()
