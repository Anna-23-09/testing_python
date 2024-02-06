# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

from functools import total_ordering


@total_ordering
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

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        raise TypeError

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        raise TypeError

    def __str__(self):
        return f'{self.width = } {self.long = }'


r1 = Rectangle(6, 7)
r2 = Rectangle(3, 6)

print(r1 == r2)
print(r1 > r2)
