my_list = [2, 4, 6, 2, 8, 10, 12, 2, 4, 14, 2]
spam = my_list.index(4)
print(spam)
eggs = my_list.index(4, spam + 1, 90) # указали диапазон поиска. 
# Ищем 4, начиная с ячейки первого входа(spam) + 1 (т е следующая ячейка после первого вхождения 4 в списокдо 90-й ячейки 
print(eggs)
err = my_list.index(3) # ValueError: 3 is not in list