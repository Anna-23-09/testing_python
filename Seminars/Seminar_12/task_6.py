"""
Изменяем класс прямоугольника.
Заменяем пару декораторов проверяющих длину и ширину
на дескриптор с валидацией размера.
"""


class Rectangle:
    def __init__(self, long, width=0):
        self.long = long
        if width == 0:
            self.width = long
        else:
            self.width = width

    def area(self):
        return self.long * self.width

    def perimetr(self):
        return (self.long + self.width) * 2

    def __add__(self, other):
        if isinstance(other, Rectangle):
            new_width = self.width + other.width
            new_long = self.long + other.long
            return Rectangle(new_width, new_long)
        raise TypeError

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            if self.width > other.width and self.long > other.long:
                new_width = self.width - other.width
                new_long = self.long - other.long
                return Rectangle(new_width, new_long)
            raise ValueError
        raise ValueError

    def __str__(self):
        return f'{self.width = } {self.long = }'


class ValidateSize:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Значение не может быть отрицательным")
        instance.__dict__[self.name] = value


r1 = Rectangle(3, 4)
print(r1.perimetr())
print(r1.area())
print(r1)
print(repr(r1))

r2 = Rectangle(5, 6)

r3 = r1.add(r2)
print(r3)
print(repr(r3))
