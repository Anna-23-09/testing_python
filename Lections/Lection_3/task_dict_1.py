a = {'one': 42, 'two': 3.14, 'ten': 'Hello, world!'}
b = dict(one=42, two=3.14, ten='Hello, world!')
c = dict([('one', 42), ('two', 3.14), ('ten', 'Hello, world!')]) # передаем список, состоящий из кортежей, в каждом по 2 элемента
print(a == b == c)
print(a)
print(b)
print(c)
