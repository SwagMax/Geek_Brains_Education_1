'''2. Реализовать класс Road (дорога).
    ● определить атрибуты: length (длина), width (ширина);
    ● значения атрибутов должны передаваться при создании экземпляра класса;
    ● атрибуты сделать защищёнными;
    ● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
    ● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
    дороги асфальтом, толщиной в 1 см*число см толщины полотна;
    ● проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
'''

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_full_profit(self, weight=25, thickness=10):
        # return f'Длина в метрах: {self._length} \n' \
        #        f'Ширина в метрах: {self._width} \n' \
        #        f'Масса асфальта для покрытия 1 кв. м толщиной в 1 см: {weight} \n' \
        #        f'Толщина покрытия: {thickness}' \
        #        f'{self._length} м * {self._width} м * {weight} кг * {thickness} см = ' \
        #        f'{(self._length * self._width * weight * thickness) / 1000} т.'

        return f'''\
Длина в метрах: {self._length}
Ширина в метрах: {self._width}
Масса асфальта для покрытия 1 кв. м толщиной в 1 см: {weight}
Толщина покрытия: {thickness}
___________________________________
{self._length} м * {self._width} м * {weight} кг * {thickness} см = {(self._length * self._width * weight * thickness) / 1000} т.
'''
road_1 = Road(5000, 20)
print(road_1.get_full_profit())