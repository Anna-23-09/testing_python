my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.setdefault('five')
print(f'{spam = }\t{my_dict =}')
eggs = my_dict.setdefault('six', 6)
print(f'{eggs = }\t{my_dict =}')
new_spam = my_dict.setdefault('two')
print(f'{new_spam = }\t{my_dict =}')
new_eggs = my_dict.setdefault('one', 1_000) # значение не поменяется, т к такой ключ уже существует со значением 1
print(f'{new_eggs = }\t{my_dict =}')
