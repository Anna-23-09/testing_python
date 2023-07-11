my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.add(9) # по возрастанию
print(my_set)
my_set.add(7) # 7 не добавится
print(my_set)
# my_set.add(9, 10) # TypeError: set.add() takes exactly one argument (2 given) 
my_set.add((9, 10)) # Если нужно добавить несколько элементов, то как кортеж в (())
print(my_set) # кортеж - это 1 элемент в множестве
