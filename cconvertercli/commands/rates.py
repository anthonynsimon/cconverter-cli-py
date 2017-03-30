def get_rates(api_client, currency):
    try:
        result = api_client.get_rates(currency)
        print('--------------------------')

        print('Base Currency:\t{base}'.format(base=result.base))
        print('Date:\t\t\t{0}\n'.format(result.date))

        for key, value in result.rates.items():
            print('{code}:\t\t\t{amount}'.format(code=key, amount=value))

        print('--------------------------')
    except Exception as e:
        print('error: {0}'.format(e))
