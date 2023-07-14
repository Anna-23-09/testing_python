data = ["один", "два", "три", "четыре", "пять", "шесть", "семь"]
a, b, c, *d = data # во все переменные добавится по 1 элементу, тот который со * возьмет в себя все остальные в виде списка
print(f'{a=} {b=} {c=} {d=}') # это упаковка

a, b, *c, d = data
print(f'{a=} {b=} {c=} {d=}') # также

a, *b, c, d = data
print(f'{a=} {b=} {c=} {d=}') # также

*a, b, c, d = data
print(f'{a=} {b=} {c=} {d=}') # *-ой можно пометить только 1 переменную
