"""
3.
*(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса
дату, которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте,
как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
"""

from requests import get, utils
from datetime import datetime, date

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)
# print(content.split('ID'))
my_list = content.split('ID')


def currency_rates(val):

    for i_str in my_list:
        if val in i_str:
            RUB = float(i_str.split('Value')[1].strip('></').replace(',', '.'))
            print(RUB, type(RUB))

        if 'Date' in i_str:
            i_str = i_str.split()
            print(i_str)
            for j in i_str:
                if 'Date=' in j:
                    j = j.split('"')[1].split('.')
                    d = date(int(j[2]), int(j[1]), int(j[0]))
                    print(d, type(d))
    return RUB, d

print(currency_rates('USD'))
