import requests

from cconvertercli.model import ExchangeRates, ConversionResult


class HttpClient(object):
    def __init__(self, base_url):
        self.__base_url = base_url

    def get_rates(self, base_currency):
        uri = 'rates/{c}'.format(c=base_currency)
        response = self.__api_request(uri)
        result = ExchangeRates.decode_json(response.json())
        return result

    def convert(self, from_currency, to_currency, amount):
        uri = 'convert?from={f}&to={t}&amount={a}'.format(f=from_currency, t=to_currency, a=amount)
        response = self.__api_request(uri)
        result = ConversionResult.decode_json(response.json())
        return result

    def __api_request(self, uri):
        response = requests.get('{base}/api/{uri}'.format(base=self.__base_url, uri=uri))

        if response.status_code != 200:
            raise Exception('API response not ok:', response.text)

        return response
