from django.urls import path, include
from users.views.users import UserDetailView, PinnedChatView
from users.views.sign_up import SignUpView
from users.views.sign_in import SignInView
from users.views.sign_out import SignOutView
from users.views.referrals import SignUpWithReferralView


urlpatterns = [
    path('sign-up', SignUpView.as_view(), name='signup'),
    path('sign-in', SignInView.as_view(), name='signin'),
    path('sign-out', SignOutView.as_view(), name='sign-out'),
    path('register/<str:referral_code>', SignUpWithReferralView.as_view(), name='register-with-referral'),
    path('user/', include([
        path('detail', UserDetailView.as_view(), name='user-detail'),
        path("pinned-chat", PinnedChatView.as_view(), name="pinned-chat-list"),
    ])),
]
