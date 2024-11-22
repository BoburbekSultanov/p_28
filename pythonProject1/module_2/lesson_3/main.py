class A:
    def __init__(self):
        self.a = 2
        self._b = 3

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value

    @property
    def __dict__(self):
        return "Ma'lumot yo`q"


obj = A()
obj.b = 10
print(obj.b)


