my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.get('two')) # передаем ключ
print(my_dict.get('five')) # передаем ключ, которого нет. Получаем None
print(my_dict.get('five', 5)) # передаем ключ, которого нет. Значение по умолчанию = 5. Вернется это значение
print(my_dict.get('ten', 5)) # значение по умолчанию не понадобилось, т к есть ключ 'ten'
