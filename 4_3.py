"""
3.
*(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса
дату, которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте,
как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
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

print(currency_rates(input('Введи валюту:\n')))
