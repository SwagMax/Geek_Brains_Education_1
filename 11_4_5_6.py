''' 4. Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад. А также
класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведённых типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

    5. Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают за
приём оргтехники на склад и передачу в определённое подразделение компании. Для
хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру (например, словарь).

    6. Продолжить работу над предыдущим заданием. Реализовать механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.'''


class Storage:
    def __init__(self):
        self.stor_dict = {}

    def get(self, equipment):
        self.stor_dict.setdefault(equipment.type_name(), []).append(equipment)

    def set(self, model):
        if self.stor_dict[model]:
            self.stor_dict.setdefault(model).pop(0)


class Equipment:
    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.type_eq = self.__class__.__name__

    def type_name(self):
        return f'{self.type_eq}'

    def __repr__(self):
        return f'{self.model} {self.year}'


class Printer(Equipment):
    def __init__(self, serial, name, year):
        super().__init__(name, year)
        self.series = serial


class Scaner(Equipment):
    def __init__(self, serial, name, year):
        super().__init__(name, year)
        self.series = serial


class Copier(Equipment):
    def __init__(self, serial, name, year):
        super().__init__(name, year)
        self.series = serial


stor = Storage()

scaner = Scaner(125, 'DNS', 2010)
stor.get(scaner)

scaner = Scaner(126, 'DNS', 2011)
stor.get(scaner)

scaner = Scaner(25632, 'DNS', 2012)
stor.get(scaner)

printer = Printer(2564, 'EPSON', 2018)
stor.get(printer)

copier = Copier(1256, 'Kyocera', 2020)
stor.get(copier)


print(f'Склад до передачи: {stor.stor_dict}')

stor.set('Scaner')
stor.set('Copier')
stor.set('Printer')

print(f'Склад после передачи: {stor.stor_dict}')