# cconverter-cli-py

CLI for currency exchange rate querying and conversion.

## Setup

Simply clone the repo and feed the cconvertercli module to the python interpreter:

```
$ git clone https://github.com/anthonynsimon/cconverter-cli-py
$ cd cconverter-cli-py
$ python -m cconvertercli -h
usage: cconvertercli [-h] [--apihost APIHOST] {rates,convert,normalize} ...

positional arguments:
  {rates,convert,normalize}
    rates               get the latest rates
    convert             convert an amount between currencies
    normalize           normalize a csv file

optional arguments:
  -h, --help            show this help message and exit
  --apihost APIHOST     the API's host:port address

```

## Usage

Make sure that the [API server](https://github.com/anthonynsimon/cconverter-api-finatra) is already up and running at this point.

For convinience, the CLI assumes that the companion API server is running on `localhost:8080`. But you can config that, simply use the `--apihost`
flag, like so:
```
cconverter --apihost=myhost:myport <subcommand> <subcommand args>
```

### Normalize CSV files

If someone happens to want to normalize the prices of a CSV file, and the layout looks
something like this:

```
item,price,currency
B,9.99,USD
C,0.99,GBP
A,10.99,EUR
```

You can simply use the following command:

```
$ cconverter normalize --filepath=FILE_PATH --target=CURRENCY --output=OPTIONAL_DESTINATION_PATH

# Help for normalize command
$ python -m cconvertercli normalize -h
usage: cconvertercli normalize [-h] -f FILEPATH -t TARGET -o OUTPUT

optional arguments:
  -h, --help            show this help message and exit
  -f FILEPATH, --filepath FILEPATH
                        the path to the source csv file
  -t TARGET, --target TARGET
                        the target currency
  -o OUTPUT, --output OUTPUT
                        the output csv file


```

Example:

```
$ cat myfile.csv
item,price,currency
B,9.99,USD
C,0.99,GBP
A,10.99,EUR

$ python -m cconvertercli normalize --filepath=./myfile.csv --target=gbp --output=./normalized.csv
Normalized 9.99 USD to 1110.7881 JPY
Normalized 0.99 GBP to 137.1546 JPY
Normalized 10.99 EUR to 1312.0961 JPY

$ cat normalized.csv
item,price,currency
B,1110.7881,JPY
C,137.1546,JPY
A,1312.0961,JPY
```

### Convert between currencies

To convert from a base currency to any other supported currency:

```
$ python -m cconvertercli convert --base=BASE_CURRENCY --target=TARGET_CURRENCY --amount=PRICE
```
Example:

```
$ python -m cconvertercli convert --base=usd --target=eur --amount=100
--------------------------
From Currency:	EUR
To Currency:	USD
Amount:			100
Exchange Rate:	1.0737
Result:			107.37
--------------------------
```

### Query Exchange Rates

To query rates for any supported base currency:

```
$ cconverter rates -currency=CURRENCY
```
Example:

```
$ python -m cconvertercli rates --currency=usd
--------------------------
Base Currency:	EUR
Date:			2017-03-30 00:00:00

HRK:			7.448
USD:			1.0737
CHF:			1.0698
MXN:			20.123
RUB:			60.338
RON:			4.5448
PLN:			4.2233
NZD:			1.5304
IDR:			14297.0
SGD:			1.4977
CAD:			1.432
HUF:			309.35
MYR:			4.7463
BGN:			1.9558
BRL:			3.3555
CNY:			7.3973
NOK:			9.1695
JPY:			119.39
KRW:			1199.1
PHP:			53.865
HKD:			8.345
ZAR:			13.816
THB:			36.951
AUD:			1.3988
GBP:			0.8618
SEK:			9.5623
ILS:			3.8914
CZK:			27.022
INR:			69.691
DKK:			7.4386
TRY:			3.9119
--------------------------
```

It currently supports the following currency codes (case insensitive):

`AUD`, `BGN`, `BRL`, `CAD`, `CHF`, `CNY`, `CZK`, `DKK`, `GBP`, `HKD`, `HRK`, `HUF`,
`IDR`, `ILS`, `INR`, `JPY`, `KRW`, `MXN`, `MYR`, `NOK`, `NZD`, `USD`, `PHP`, `PLN`,
`RON`, `RUB`, `SEK`, `SGD`, `THB`, `TRY`, `ZAR`, `EUR`.
