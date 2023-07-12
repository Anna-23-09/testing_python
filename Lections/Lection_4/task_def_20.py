# Локальные переменные


def func(y:int) ->int:
    x = 100
    # x += 100 # UnboundLocalError: local variable 'x' referenced before assignment
    print(f'In func {x = }')
    return y + 1


x = 42
print(f'In main {x = }')
z = func(x)
print(f'{x = }\t{z = }')
