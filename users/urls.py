from django.urls import path, include
from users.views.users import *

# from users.views import UserCreateView, UserDetailView


urlpatterns = [
    # path('user/', include([
    #     path('detail/<int:user_id>', UserDetailView.as_view(), name='user-detail'),
    #     path('create/', UserCreateView.as_view(), name='user-create'),
    # ]))
    path('present/', include([
        path('money/', include([
            path('create/', PresentMoneyCreateView.as_view()),
            path('detail/<int:transaction_id>', PresentMoneyDetailView.as_view())
        ])),
        path('badge/', include([
            path('create/', PresentBadgeCreateView.as_view()),
            path('detail/<int:badge_id>', PresentBadgeDetailView.as_view())
        ])),
        path('verification/', include([
            path('create/', PresentVerificationCreateView.as_view()),
            path('detail/<int:verification_label_id>', PresentVerificationDetailView.as_view())
        ])),
        path('subscription/', include([
            path('create/', PresentSubscriptionPlanCreateView.as_view()),
            path('detail/<int:sub_plan_id>', PresentSubscriptionPlanDetailView.as_view())
        ]))
    ]))
]