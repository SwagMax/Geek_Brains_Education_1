'''class Transport:
    def transport_method(self):
        print("Родительский метод класса Transport")

class Auto(Transport):
    def auto_method(self):
        print("Дочерний метод класса Auto")

class Bus(Transport):
    def bus_method(self):
        print("Дочерний метод класса Bus")

a = Auto()
a.transport_method()
a.auto_method()
print()
b = Bus()
b.transport_method()'''

#_________________________________________________________________

'''class Player:
    def player_method(self):
        print("Родительский метод класса Player")

class Navigator:
    def navigator_method(self):
        print("Родительский метод класса Auto")

class MobilePhone(Player, Navigator):
    def mobile_phone_method(self):
        print("Дочерний метод класса MobilePhone")

a = MobilePhone()
a.player_method()
a.mobile_phone_method()'''

#______________________________________________________________

class Shape:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    def get_params(self):
        return f'Параметры Shape: {self.param_1}, {self.param_2}'



class Material:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    def get_params(self):
        return f'Параметры Material: {self.param_1}, {self.param_2}'

class Triangle(Material, Shape):
    pass


t = Triangle(10, 20)
print(t.get_params())
