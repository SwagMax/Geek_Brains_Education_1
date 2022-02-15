'''5. Реализовать класс Stationery (канцелярская принадлежность):
    ● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
    сообщение «Запуск отрисовки»;
    ● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
    ● в каждом классе реализовать переопределение метода draw. Для каждого класса
    метод должен выводить уникальное сообщение;
    ● создать экземпляры классов и проверить, что выведет описанный метод для каждого
    экземпляра.'''


class Stationery:
    def __init__(self, title = 'Канцелярская принадлежность'):
        self.title = title

    def draw(self):
        print(f'Начни рисовать! {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Начни рисовать вместе с ручкой \033[33m{self.title}\033[0m!')


class Pencil(Stationery):
    def draw(self):
        print(f'Начни рисовать вместе с карандашем \033[3m{self.title}\033[0m!')


class Handle(Stationery):
    def draw(self):
        print(f'Начни рисовать вместе с маркером \033[43m{self.title}\033[0m!')


stat = Stationery()
pen = Pen('"Parker"')
pencil = Pencil('"Художник"')
handle = Handle('"PAINT Marker"')

office_supplies = [stat, pen, pencil, handle]

for i in office_supplies:
    i.draw()