"""all(iterables)"""


def all_(iterable):
    for element in iterable:
        if not element:
            return False
    return True


numbers = [42, -73, 0, 1024]
if all(map(lambda x: x > 0, numbers)):
    print("Все элементы положительные")
else:
    print("В последовательности есть отрицательныеи/или нулевые элементы")
