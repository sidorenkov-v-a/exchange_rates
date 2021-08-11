from django.urls import include, path
from django.views.generic import RedirectView
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


from .router import RateRouter
from .views import RateViewSet

router = RateRouter()
router.register('rates', RateViewSet)

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='currencies-list')),
    path('auth/', obtain_auth_token, name='auth'),
    path('', include(router.urls)),
]

schema_view = get_schema_view(
    openapi.Info(
        title='API проекта Exchange rates',
        default_version='v1',
        description='Проект выполнен в рамках тестового задания',
        contact=openapi.Contact(
            name='Владислав',
            email='sidorenkov.v.a@yandex.ru',
            url='https://github.com/sidorenkov-v-a',
            telegram='https://t.me/sidorenkov_vl'
        ),
        license=openapi.License(name='MIT License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]
