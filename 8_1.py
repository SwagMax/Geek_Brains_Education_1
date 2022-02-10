'''1. Написать функцию email_parse(<email_address>), которая при помощи регулярного
выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в
виде словаря. Если адрес не валиден, выбросить исключение ValueError.
Пример:

    >>> email_parse('someone@geekbrains.ru')
    {'username': 'someone', 'domain': 'geekbrains.ru'}
    >>> email_parse('someone@geekbrainsru')
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        ...
            raise ValueError(msg)
    ValueError: wrong email: someone@geekbrainsru

Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном
выражении; имеет ли смысл в данном случае использовать функцию re.compile()?'''

import re


def email_parse(email_address):
    parse_email = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not parse_email.match(email_address):
        raise ValueError(f'Неверный адрес: {email_address}')
    print(parse_email.match(email_address).groupdict())


for _ in ['someone@geek.ru', 'some&one@geek.ru', 'someone@geekru']:
    try:
        email_parse(_)
    except ValueError as err:
        print(err)