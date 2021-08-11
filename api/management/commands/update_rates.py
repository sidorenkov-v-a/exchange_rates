import requests
from django.core.management import BaseCommand

from api.models import Currency


class Command(BaseCommand):

    def handle(self, *args, **options):
        response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        data = response.json()
        currencies = data['Valute']
        for currency in currencies.values():
            name = currency['Name']
            rate = currency['Value']
            defaults = {'name': name, 'rate': rate}
            Currency.objects.update_or_create(name=name, defaults=defaults)
