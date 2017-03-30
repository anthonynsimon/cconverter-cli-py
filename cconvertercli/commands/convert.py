def convert(api_client, base, target, amount):
    try:
        result = api_client.convert(base, target, amount)
        print('--------------------------')

        print('From Currency:\t{0}'.format(result.from_currency))
        print('To Currency:\t{0}'.format(result.to_currency))
        print('Amount:\t\t\t{0}'.format(result.amount_to_convert))
        print('Exchange Rate:\t{0}'.format(result.exchange_rate))
        print('Result:\t\t\t{0}'.format(result.conversion_result))

        print('--------------------------')
    except Exception as e:
        print('error: {0}'.format(e))
