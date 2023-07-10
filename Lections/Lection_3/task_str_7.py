pi = 3.1415
print(f'Число Пи с точностью 2 знака: {pi:.2f}') # после точки 2 знака типа float

data = [3254, 436414532, 43465474, 2342, 462256, 1747]
for item in data:
    print(f'{item:>10}')

num = 2 * pi * data[1]
print(f'{num = :_}')
