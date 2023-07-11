my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.pop('two')
print(f'{spam = }\t{my_dict=}')
# err = my_dict.pop('six') # ключ 'six' не входит в my_dict
err = my_dict.pop() # pop expected at least 1 argument, got 0 Нет аргумента, он ДОЛДЕН БЫТЬ (ключ)
