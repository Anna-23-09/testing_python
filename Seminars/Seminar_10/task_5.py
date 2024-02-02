# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.special = None

    def get_special(self):
        return self.special

    def get_info(self):
        return f'{self.name = }, {self.age = }, {self.weight = }'


class Bird(Animal):
    def __init__(self, age, weight, name, colour):
        super().__init__(age, weight)
        self.special = colour


class Fish(Animal):
    def __init__(self, age, weight, name, deep):
        super().__init__(age, weight, deep)
        self.special = deep


fish = Fish(2, 0.1, 'Guppi', 15)
print(fish.get_info())
print(fish.get_special())
