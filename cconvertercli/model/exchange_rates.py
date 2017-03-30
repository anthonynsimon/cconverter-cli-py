import datetime


class ExchangeRates(object):
    def __init__(self, base, date, rates):
        self.base = base
        self.date = date
        self.rates = rates

    def decode_json(obj):
        if all(k in obj for k in ('base', 'date', 'rates')):
            date = datetime.datetime.strptime(obj['date'], '%Y-%m-%d')
            return ExchangeRates(obj['base'], date, obj['rates'])
        else:
            raise Exception('couldn\'t decode json object')
