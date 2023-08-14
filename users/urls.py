from django.urls import path, include
from users.views.users import UserDetailView
from users.views.sign_up import SignUpView
from users.views.sign_in import SignInView
from users.views.referral_code import ReferralCodeAPI


urlpatterns = [
    path('sign-up', SignUpView.as_view(), name='signup'),
    path('sign-in', SignInView.as_view(), name='signin'),
    path('user/', include([
        path('detail', UserDetailView.as_view(), name='user-detail')
    ])),
    path('login/<str:referral>/', ReferralCodeAPI.as_view(), name="referral_code"), 
    # path("pinneds", PinnedChatView.as_view(), name="pinned-list"),
    # path("pinned/<int:pinned_id/>", PinnedChatView.as_view(), name="pinned-detail"),
]
