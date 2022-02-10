'''3. Написать декоратор для логирования типов позиционных аргументов функции, например:
    def type_logger...
        ...


    @type_logger
    def calc_cube(x):
        return x ** 3


    >>> a = calc_cube(5)
    5: <class 'int'>

Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете
ли вы вывести тип значения функции? Сможете ли решить задачу для именованных
аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя
функции, например, в виде:
    >>> a = calc_cube(5)
    calc_cube(5: <class 'int'>)'''

from functools import wraps


def type_logger(function):
    @wraps(function)
    def my_function(*args, **kwargs):
        num_list = [_ for _ in (*args, *kwargs.values())]
        n = [f'{function.__name__}({el}: {type(el)})' for el in num_list]
        print (*n, *function(*args, **kwargs), sep=',\n')

    return my_function


@type_logger
def calc_cube(*x, **y):
    '''Возводит в куб принимаемое значение, если аргументов несколько - выводит через запятую!

    :param x: аргументы
    :param y: именованные аргументы
    '''
    num_list = [__ for __ in (*x, *y.values()) if isinstance(__, int) or isinstance(__, float)]
    return [i ** 3 for i in num_list]

a = calc_cube(5, 11, 8.9, 34, age=89.8, num=6)
print(calc_cube.__name__)
help(calc_cube)