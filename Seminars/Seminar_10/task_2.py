# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

from math import pi


class Rectangle:
    def __init__(self, long, width=0):
        self.long = long
        if width == 0:
            self.width = long
        else:
            self.width = width

    def square(self):
        return self.long * self.width

    def perimetr(self):
        return (self.long + self.width) * 2


x = Rectangle(2, 3)

print(x.square())
print(x.perimetr())
