from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.signals import social_account_added, pre_social_login

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from users.models import Project, ProjectData
from users.utils.users import get_user_by_github_login

from core.models import S3Attachment


@receiver(social_account_added, sender=SocialAccount)
def add_user_via_social_account(sender, instance, **kwargs):
    print('SOCIAL ACCOUNT ADDED')
    print(sender)
    print(instance)
    print(kwargs)


def add_projects_via_github(data, repo_ids: list = None):
    user = get_user_by_github_login(data[0]['owner']['login'])
    if user:
        if repo_ids:
            data = [repo for repo in data if repo.get('id') in repo_ids]

        project_objects = []
        for repo in data:
            project_objects.append(
                Project(
                    name=repo.get('name'),
                    description=repo.get('description'),
                    price=0,
                    author=user,
                    is_active=False
                )
            )
        projects = Project.objects.bulk_create(project_objects)

        projects_data = []
        for project in projects:
            projects_data.append(
                ProjectData(
                    provider=ProjectData.GITHUB,
                    project=project,
                    data=data
                )
            )
        ProjectData.objects.bulk_create(projects_data)

