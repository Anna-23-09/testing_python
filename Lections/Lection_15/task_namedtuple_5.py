from collections import namedtuple


Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
data = [Point(2, 202, 4), Point(10, -100, -500), Point(3, 7, 11), Point(2, 3, 1)]
print(sorted(data))     # сортировка сначала по x, потом по y, потом по z
