''' 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый — с
декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число». Второй — с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.'''

class Date:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def extraction(cls, date):
        date_list = []

        for _ in date.split():
            if _ != '-':
                date_list.append(_)

        return int(date_list[0]), int(date_list[1]), int(date_list[2])

    @staticmethod
    def validation(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 9999 >= year >= 0:
                    return f'Дата введена правильно \N{winking face}'
                else:
                    return f'Не правильно введен год {year} \N{grinning face}'
            else:
                return f'Не правильно введен месяц {month} \N{grinning face}'
        else:
            return f'Не правильно введен день {day} \N{grinning face}'

    def __str__(self):
        return f'Текущая дата {Date.extraction(self.date)}'


today = Date('19 - 02 - 2022')
print(today)

print(Date.validation(19, 2, 2022))
print(today.validation(19, 2, 2022))

print(Date.extraction('19 - 02 - 2022'))
print(today.extraction('19 - 02 - 2022'))

print(Date.validation(19, 45, 2022))
print(today.validation(40, 2, 2022))



