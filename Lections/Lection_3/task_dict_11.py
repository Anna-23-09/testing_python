my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
my_dict.update(dict(six=6))
print(my_dict)
my_dict.update(dict([('five', 5), ('two', 2)])) # 'two' уже есть, он не добавится
print(my_dict)

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
new_dict = my_dict | {'five': 5, 'two': 42} |dict(six=6) # 'two' поменялась на 42, остальное просто добавилось в конец
print(new_dict)
