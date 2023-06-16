from django.urls import path
from users.views import UserCreateView

from .views import ProjectCreateListAPIView,ProjectRetriveUpdateDeleteAPIView,ClientCreateListAPIView,ClientRetriveUpdateDeleteAPIView,TeamCreateListAPIView,TeamRetriveUpdatedeleteAPIView


urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-create'),
    path('projects/',ProjectCreateListAPIView.as_view(),name='project-creat-list-view'),
    path('project/<int:pk>/',ProjectRetriveUpdateDeleteAPIView.as_view(),name='project-update-delete-view'),
    path('clients/',ClientCreateListAPIView.as_view(),name='client-create-list-view'),
    path('client/<int:pk>/',ClientRetriveUpdateDeleteAPIView.as_view(), name='client-update-delete-view'),
    path('teams/',TeamCreateListAPIView.as_view(),name='team-update-delete-view'),
    path('team/<int:pk>/',TeamRetriveUpdatedeleteAPIView.as_view(),name='team-update-delete-view')
]

