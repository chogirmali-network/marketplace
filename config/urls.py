from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view as drf_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from main.views import QuestionViewSet, AnswerViewSet, NotificationsViewSet

schema_view = drf_schema_view(
    openapi.Info(
        title='Cybersell',
        description='Cybersell API documentation for developers',
        default_version='v1',
        terms_of_service='https://www.google.com/policies/terms',
        contact=openapi.Contact(email='chogirmali.yigit@gmail.com')
    ),
    public=True,
    permission_classes=(AllowAny, )
)
"""
Azamatni chiqargan kodi. urllarni o'ziz do'g'irlabaring
"""
router = DefaultRouter()
router.register(r'questions',QuestionViewSet,basename='questions')
router.register(r'answers',AnswerViewSet,basename='answers')
router.register(r'notifications',NotificationsViewSet,basename='notifications')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-doc'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-doc'),
    path('api/v1/',include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)