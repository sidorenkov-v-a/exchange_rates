import requests
from django.core.management import BaseCommand

from api.models import Currency


class Command(BaseCommand):
    def handle(self, *args, **options):
        Currency.objects.all().delete()
        response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        data = response.json()
        currencies = data['Valute']
        objs = []
        for currency in currencies.values():
            objs.append(
                Currency(name=currency['Name'], rate=currency['Value'])
            )
        Currency.objects.bulk_create(objs)
