class MyClass:
    def __setattr__(self, key, value):
        if key == "one":
            self.__dict__[key] = value
            print(self.__dict__)
        else:
            print("err")

a = MyClass()
a.one = 11
a.two = 12