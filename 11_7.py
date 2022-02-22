'''7. Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное
число». Реализовать перегрузку методов сложения и умножения комплексных чисел.
Проверить работу проекта. Для этого создать экземпляры класса (комплексные числа),
выполнить сложение и умножение созданных экземпляров. Проверить корректность
полученного результата.'''


class Complexus:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма = {self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        return f'Произведение = {self.a * other.a - self.b * other.b} + {self.b * other.a + self.a * other.b}i'

    def __str__(self):
        return f'Комплексное число: {self.a} + {self.b}i'


c = Complexus(15, -1)
d = Complexus(5, 4)
print(c)
print(d)
print(c + d)
print(c * d)