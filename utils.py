"""
Currency_rates
~~~~~~~~~~~~~~~~~~~~~
Exchange rate on the date of the request
    currency_rates(val)

:copyright: (c) 2022 by SwagMax.
:license: My_dog 2.0, see LICENSE for more details.
"""
from requests import get, utils


response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)
# print(content.split('ID'))
my_list = content.split('ID')


def currency_rates(val):
    '''
    Exchange rate on the date of the request
    :param val: type "USD"
    :return: float
    '''
    for i_str in my_list:
        if val in i_str:
            RUB = float(i_str.split('Value')[1].strip('></').replace(',', '.'))
    return RUB


if __name__ == "__main__":
    print('i`m a file')
else:
    print('i`m a module util.py')
#print(currency_rates('USD'))