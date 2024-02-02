# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

from math import pi
class Circle:
    def __init__(self, val):
        self.radius = val

    def square(self):
        return 2 * pi * self.radius ** 2

    def long_circle(self):
        return 2 * pi * self.radius


x = Circle(10)

print(x.square())
print(x.long_circle())
