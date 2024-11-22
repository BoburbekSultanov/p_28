class Animal:
    def __init__(self, name, gander, habitat):
        self.name = name
        self.gander = gander
        self.habitat = habitat

    def __repr__(self):
        return f"{self.__class__.__name__}(name = {self.name}, gander = {self.gander}, habitat = {self.habitat}"


class Bird(Animal):
    def __init__(self, name, gander, habitat, fly: bool):
        super().__init__(name, gander, habitat)
        self.fly = fly

    def __repr__(self):
        return f"{self.__class__.__name__}(name = {self.name}, gander = {self.gander}, habitat = {self.habitat}, fly {self.fly})"


class Fish(Bird):
    def __init__(self, name, gander, habitat, fly: bool):
        super().__init__(name, gander, habitat, fly)


class Mammal(Animal):
    def __init__(self, name, gander, habitat):
        super().__init__(name, gander, habitat)


f1 = Fish('oltin', 'baliq', 'salom', True)
print(f1)
