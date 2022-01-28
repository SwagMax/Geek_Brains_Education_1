"""
Currency_rates
~~~~~~~~~~~~~~~~~~~~~
Exchange rate on the date of the request
    currency_rates(val)

:copyright: (c) 2022 by SwagMax.
:license: My_dog 2.0, see LICENSE for more details.
"""

from requests import get, utils
from datetime import datetime

response = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp'))


def currency_rates(val):
    '''
    Exchange rate on the date of the request
    :param val: type "USD"
    :return: float
    '''

    my_list = response.split('ID')

    for i_str in my_list:
        if val.upper() in i_str:
            print(datetime.strptime(my_list[0].split('"')[-4], '%d.%m.%Y').date(), ", ", sep="", end="")
            return float(i_str.split('Value')[1].strip('></').replace(',', '.'))


if __name__ == "__main__":
    print(currency_rates(input('Введи валюту: \n')))
