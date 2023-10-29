from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.views.generic import TemplateView

from drf_yasg.views import get_schema_view as drf_schema_view
from drf_yasg import openapi

from rest_framework.permissions import AllowAny


schema_view = drf_schema_view(
    openapi.Info(
        title='Proverse',
        description='Proverse API documentation for developers',
        default_version='v1',
        terms_of_service='https://www.google.com/policies/terms',
        contact=openapi.Contact(email='chogirmali.yigit@gmail.com')
    ),
    public=True,
    permission_classes=[AllowAny]
)


urlpatterns = [
    path('', TemplateView.as_view(template_name='dashboard/home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-doc'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-doc'),
    path("accounts/", include("allauth.urls")),
    path('api/v1/', include([
        path('users/', include(('users.urls', 'users'), namespace='users')),
        path('company/', include(('company.urls', 'company'), namespace='company')),
        path('mediafiles/', include(('mediafiles.urls', 'mediafiles'), namespace='mediafiles')),
        path('main/', include(('main.urls', 'main'), namespace='main')),
    ])),
    path('payments/', include(('payments.urls', 'payments'), namespace='payments'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
