"""iter(object[, sentinel])"""

# a = 42
# iter(a) # TypeError: 'int' object is not iterable

data = [2, 4, 6, 8]
list_iter = iter(data)
print(list_iter) # вывод: <list_iterator object at 0x000001459F058BE0>

data = [2, 4, 6, 8]
list_iter = iter(data)
print(*list_iter)
print(*list_iter) # вывод списка только 1 раз без [] и , 
