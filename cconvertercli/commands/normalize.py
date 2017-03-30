import csv


def normalize(api_client, filepath, target_currency, output):
    try:
        with open(filepath, 'r') as in_file:
            with open(output, 'w') as out_file:
                reader = csv.DictReader(in_file)
                writer = csv.writer(out_file, lineterminator='\n')
                writer.writerow(('item', 'price', 'currency'))
                for row in reader:
                    record = Record(row['item'], row['price'], row['currency'])
                    result = api_client.convert(record.currency, target_currency, record.amount)
                    writer.writerow((record.item, result.conversion_result, result.to_currency))
                    print('Normalized {amount} {base} to {result} {target}'.format(amount=result.amount_to_convert,
                                                                                   base=result.from_currency,
                                                                                   result=result.conversion_result,
                                                                                   target=result.to_currency))

    except Exception as e:
        print('error: {0}'.format(e))


class Record(object):
    def __init__(self, item, amount, currency):
        self.item = item
        self.amount = amount
        self.currency = currency
