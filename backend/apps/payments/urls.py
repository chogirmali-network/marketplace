from django.urls import path, include
from .views import stripe_view


urlpatterns = [
    path('pricing_page/', stripe_view, name='pricing_page'),
]