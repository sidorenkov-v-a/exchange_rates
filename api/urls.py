from django.urls import include, path
from django.views.generic import RedirectView
from rest_framework.authtoken.views import obtain_auth_token

from .router import RateRouter
from .views import RateViewSet

router = RateRouter()
router.register('rates', RateViewSet)

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='currencies-list')),
    path('auth/', obtain_auth_token, name='auth'),
    path('', include(router.urls)),
]
