"""
2.
Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты
по отношению к рублю. Использовать библиотеку requests. В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса
str, решить поставленную задачу? Функция должна возвращать результат числового типа, например float.
Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом?
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того,
в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.
"""

from requests import get, utils

response = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp'))


def currency_rates(val):
    '''
    Exchange rate on the date of the request
    :param val: like: "USD"
    :return: float
    '''

    my_list = response.split('ID')

    for i_str in my_list:
        if val.upper() in i_str:
            return float(i_str.split('Value')[1].strip('></').replace(',', '.'))

print(currency_rates(input('Введи валюту:\n')))