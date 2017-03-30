import argparse
import os 

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apihost", help='the API\'s host:port address', default='http://localhost:8080')

    subparsers = parser.add_subparsers(dest='command')
    
    rates_cmd = subparsers.add_parser('rates', help='get the latest rates')
    rates_cmd.add_argument('-c', '--currency', help='the base currency for which to get the rates')

    convert_cmd = subparsers.add_parser('convert', help='convert an amount between currencies')
    convert_cmd.add_argument('-f', '--from', help='the source currency')
    convert_cmd.add_argument('-t', '--to', help='the target currency')
    convert_cmd.add_argument('-a', '--amount', help='the amount to be converted')

    normalize_cmd = subparsers.add_parser('normalize', help='normalize a csv file')
    normalize_cmd.add_argument('-f', '--file', help='the path to the source csv file')
    normalize_cmd.add_argument('-t', '--to', help='the target currency')
    normalize_cmd.add_argument('-o', '--output', help='the output csv file', default='./normalized.csv')

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    if "CCONVERTER_DEBUG" in os.environ:
        print(args)

