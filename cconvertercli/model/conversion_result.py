class ConversionResult(object):
    def __init__(self, from_currency, to_currency, amount_to_convert, exchange_rate, conversion_result):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.amount_to_convert = amount_to_convert
        self.exchange_rate = exchange_rate
        self.conversion_result = conversion_result

    def decode_json(obj):
        if all(k in obj for k in ('fromCurrency', 'toCurrency', 'amountToConvert', 'exchangeRate', 'conversionResult')):
            return ConversionResult(obj['fromCurrency'],
                                    obj['toCurrency'],
                                    obj['amountToConvert'],
                                    obj['exchangeRate'],
                                    obj['conversionResult'])
        else:
            raise Exception('couldn\'t decode json object')
