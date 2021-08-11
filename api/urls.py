from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from .router import RateRouter
from .views import RateViewSet

router = RateRouter()
router.register('rates', RateViewSet)

urlpatterns = [
    path('auth/', obtain_auth_token, name='auth'),
    path('', include(router.urls)),
]
