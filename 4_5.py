"""
5.
*(вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли.
Например:
    > python task_4_5.py USD
    75.18, 2020-09-05
"""

from sys import argv
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
    print(currency_rates(argv[1]))