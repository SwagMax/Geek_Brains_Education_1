'''4. Реализуйте базовый класс Car:
    ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
    также методы: go, stop, turn(direction), которые должны сообщать, что машина
    поехала, остановилась, повернула (куда);
    ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
    ● добавьте в базовый класс метод show_speed, который должен показывать текущую
    скорость автомобиля;
    ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
    скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
    превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.'''

from random import choice


class Car:
    direction = ['С', 'С-В', 'В', 'Ю-В', 'Ю', 'Ю-З', 'З', 'С-З']

    def __init__(self, n, c, s, p=False):
        self.name = n
        self.color = c
        self.speed = s
        self.is_police = p
        print(f'Машина: {n} цвет {c}. \nЭто полицейская машина? {p}')

    def go(self):
        print(f'{self.name}: Поехал.')

    def stop(self):
        print(f'{self.name}: Остановился.')

    def turn(self):
        print(f'{self.name}: В направлении: {choice(self.direction)}.')

    def show_speed(self):
        return f'{self.name}: Скорость: {self.speed}.'


class TownCar(Car):

    def show_speed(self):
        return f'{self.name}: Скорость: {self.speed}. Превышение!!!' if self.speed > 60 else super().show_speed()


class WorkCar(Car):

    def show_speed(self):
        return f'{self.name}: Скорость: {self.speed}. Превышение!!!' if self.speed > 40 else super().show_speed()


class SportCar(Car):
    pass

class PoliceCar(Car):

    def __init__(self, n, c, s):
        super().__init__(n, c, s, p=True)


police_car = PoliceCar('"Козёл"', 'Полосатый', 300)
work_car = WorkCar('ЗИЛ', 'Синий', 100)
sport_car = SportCar('Ламбо', 'Белый', 120)
town_car = TownCar('Мини', 'Красный', 65)

list_of_cars = [police_car, work_car, sport_car, town_car]

for _ in list_of_cars:
    _.go()
    print(_.show_speed())
    _.turn()
    _.stop()
    print()

