import argparse

from cconvertercli import commands
from cconvertercli import httpclient


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apihost", help='the API\'s host:port address', default='http://localhost:8080')

    subparsers = parser.add_subparsers(dest='command')

    rates_cmd = subparsers.add_parser('rates', help='get the latest rates')
    rates_cmd.add_argument('-c', '--currency', help='the base currency for which to get the rates', required=True)

    convert_cmd = subparsers.add_parser('convert', help='convert an amount between currencies')
    convert_cmd.add_argument('-b', '--base', help='the base currency', required=True)
    convert_cmd.add_argument('-t', '--target', help='the target currency', required=True)
    convert_cmd.add_argument('-a', '--amount', help='the amount to be converted', required=True)

    normalize_cmd = subparsers.add_parser('normalize', help='normalize a csv file')
    normalize_cmd.add_argument('-f', '--filepath', help='the path to the source csv file', required=True)
    normalize_cmd.add_argument('-t', '--target', help='the target currency', required=True)
    normalize_cmd.add_argument('-o', '--output', help='the output csv file', default='./normalized.csv', required=True)

    return parser.parse_args()


def apply(args):
    api_client = httpclient.HttpClient(args.apihost)
    return {
        'rates': lambda: commands.get_rates(api_client, args.currency),
        'convert': lambda: commands.convert(api_client, args.base, args.target, args.amount),
        'normalize': lambda: commands.normalize(api_client, args.filepath, args.target, args.output),
        None: 'unknown command'
    }[args.command]()
