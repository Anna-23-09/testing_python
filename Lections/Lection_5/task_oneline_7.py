a = b = c = 0 # хорошо
a += 42
print(f'{a=} {b=} {c=}') # здесь изменится только a

a = b = c = {1, 2, 3} # плохо
a.add(42)
print(f'{a=} {b=} {c=}') # здесь 42 добавится в каждое множество