"""
Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
Используйте декораторы свойств.
"""


class Rectangle:
    __slots__ = ('_width', '_long')

    def __init__(self, long, width=0):
        self._long = long
        self._width = width if width else long

    def area(self):
        return self._long * self._width

    def perimetr(self):
        return (self._long + self._width) * 2

    @property
    def long(self):
        return self._long

    @property
    def width(self):
        return self._width

    @long.setter
    def long(self, value):
        if value > 0:
            self._long = value
        else:
            raise ValueError('Значение не может быть отрицательным')

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError('Значение не может быть отрицательным')


r1 = Rectangle(3, 4)
r1.long = 3
r1.width = -3
print(r1.long)
