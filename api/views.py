from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Currency
from .serializers import RateSerializer


class RateViewSet(ReadOnlyModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = RateSerializer
