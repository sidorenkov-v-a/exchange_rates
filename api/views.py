from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Currency
from .serializers import CurrencySerializer


class CurrencyViewSet(ReadOnlyModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
