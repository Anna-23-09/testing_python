data = [2, 5, 1, 42, 65, 76, 24, 77]
res = []
for item in data:
    if item % 2 == 0:
        res.append(item) # вывод четных чисел из списка
print(f'{res=}')


data = [2, 5, 1, 42, 65, 76, 24, 77]
res = [item for item in data if item % 2 == 0] # более компактная запись
print(f'{res=}')
