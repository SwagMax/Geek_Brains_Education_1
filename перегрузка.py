class MyClass:
    def __init__(self, param, param_2):
        self.param = param
        self.param_2 = param_2

    def __str__(self):
        return f'param: {self.param}, param_2: {self.param_2}'

    def __add__(self, other):
        # return self.param + other.param, self.param_2 + other.param_2
        return MyClass(self.param + other.param, self.param_2 + other.param_2)

    # def __del__(self):
    #     print("Deleted")


mc = MyClass(77, 88)
mcc = MyClass(100, 200)
# del mc
print(mc + mcc+mcc)