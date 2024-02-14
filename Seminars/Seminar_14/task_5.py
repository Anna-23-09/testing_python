"""
На семинарах по ООП был создан класс прямоугольник
хранящий длину и ширину, а также вычисляющую периметр,
площадь и позволяющий складывать и вычитать
прямоугольники беря за основу периметр.
Напишите 3-7 тестов unittest для данного класса.
"""
from functools import total_ordering
import unittest
class Rectangle:

    def __init__(self, side_a, side_b = None):
        self.side_a = side_a
        self.side_b = side_b if side_b else side_a

    def perimeter(self):
        return (self.side_a + self.side_b) * 2

    def area(self):
        return self.side_a * self.side_b

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.side_a == other.side_a and self.side_b == other.side_b
        return TypeError

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        return TypeError

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.side_a + other.side_a, self.side_b + other.side_b)
        return TypeError


class RectangleTest(unittest.TestCase):

    def setUp(self) -> None:
        self.rectangle_test =Rectangle (4, 5)
        self.rectangle_another = Rectangle(5, 10)

    def test_equals(self):
        self.assertTrue(self.rectangle_test, Rectangle(4, 5))

    def test_add(self):
        self.assertTrue(self.rectangle_test + self.rectangle_another, Rectangle(9, 15))

    def test_lesser(self):
        self.assertTrue(self.rectangle_test < self.rectangle_another)

    def test_perimeter(self):
        self.assertTrue(self.rectangle_test, 18)

    def test_area(self):
        self.assertEqual(self.rectangle_another, 50)


if __name__ == '__main__':
    unittest.main(verbosity=2)
