# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем длину и ширину.
# При вычитании не допускайте отрицательных значений.


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


r1 = Rectangle(6, 7)
r2 = Rectangle(3, 5)

print(r1 + r2)
print(r1 - r2)
