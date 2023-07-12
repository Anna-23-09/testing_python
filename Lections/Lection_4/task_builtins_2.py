"""filter(function, iterable)"""
numbers = [42, -72, 1024]
res = tuple(filter(lambda x: x > 0, numbers))
print(res)
