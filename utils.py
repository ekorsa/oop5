import json
import requests

import config
from config import keys, API_KEY


class ConversionException(Exception):
    pass


class ConversionCurrency:
    @staticmethod
    def convert(base, target, amount):
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConversionException(f'Unknown currency: {base}')

        try:
            target_ticker = keys[target]
        except KeyError:
            raise ConversionException(f'Unknown currency: {target}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f'Wrong amount: {amount}, it should be digit.')

        request = requests.get(f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{keys[base]}/{keys[target]}')
        data = json.loads(request.content)
        new_amount = float(data['conversion_rate']) * float(amount)
        return new_amount
