class Auto:
    # атрибуты класса
    #auto_name = "Lexus"
    #auto_model = "RX 350L"
    #auto_year = 2019
    counter = 0


    # конструктор

    def __init__(self, n, m, y):
        self.auto_name = n
        self.auto_model = m
        self.auto_year = y
        # self.on_auto_start()

        Auto.counter += 1
        print(f'New example of class Auto: {self.counter}') #печатает заголовок при каждом создании ЭКЗЕМПЛЯРА КЛАССА

    # методы класса
    def on_auto_start(self, speed):
        print(f"Заводим автомобиль {self.auto_name} with {speed}")

    def on_auto_stop(self):
        print(f"Останавливаем работу двигателя {self.auto_model}")

a = Auto('Mazda', 'cx0', 2021)
# print(a)
# print(type(a))
# print(a.auto_name)
a.on_auto_start(50)
# a.on_auto_stop()
# print(a.counter)

b = Auto('lada', '12', 202323132)
# print(b)
# print(type(b))
# #b.auto_name = 'Mazda'
# print(b.auto_name)
b.on_auto_start(12)
# b.on_auto_stop()
# print(b.counter)
