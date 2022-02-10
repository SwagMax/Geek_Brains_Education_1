'''
3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь,
разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь
в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше
записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из
скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз
меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
    Иванов,Иван,Иванович
    Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
    скалолазание,охота
    горные лыжи
'''

from json import dump
from itertools import zip_longest

with open('users.csv', encoding='utf-8') as users:
    with open('hobby.csv', encoding='utf-8') as hobby:

        if len(users.readlines()) >= len(hobby.readlines()):
            users.seek(0)
            hobby.seek(0)
            with open('result.json', 'w', encoding='utf-8') as result:
                result_list = zip_longest((' '.join(_.split(',')) for _ in users), hobby, fillvalue=None)
                result_dict = {str(__[0]).strip(): str(__[1]).strip() for __ in result_list}

                dump(result_dict, result, ensure_ascii=False, indent=4)
            print(result_dict)
        else:
            exit(1)