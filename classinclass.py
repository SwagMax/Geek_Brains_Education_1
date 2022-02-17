class Transport:
    # конструктор
    def __init__(self, n, m, y):
        self.auto_name = n
        self.auto_model = m
        self.auto_year = y

    # методы класса
    def on_auto_start(self, speed):
        print(f"Заводим автомобиль {self.auto_name} with {speed}")

    def on_auto_stop(self):
        print(f"Останавливаем работу двигателя {self.auto_model}")

class Auto(Transport):
    def __init__(self, n, m, y, p):
        # self.auto_name = n
        # self.auto_model = m
        # self.auto_year = y

        # super().__init__(n, m, y)
        Transport.__init__(self, n, m, y)

        self.passengers = p

    def drift(self):
        print("Vgggg")


# auto_1 = Auto()


#
a = Auto('Mazda', 'cx0', 2021, 5)
a.on_auto_start(50)
a.drift()
print(a.passengers)
#
print()
#
b = Auto('lada', '12', 2023, 9868)
b.on_auto_start(12)
print(b.auto_year)

