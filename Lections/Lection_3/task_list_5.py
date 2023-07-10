my_list = [2, 4, 6, 8, 10, 12]
spam = my_list.pop() # удаляет правый объект из списка. В нашем случае это 12. Кроме того, мы 12 схранили в переменную "spam"
print(spam, my_list)
eggs = my_list.pop(1)
print(eggs, my_list)
err = my_list.pop(10) # IndexError: pop index out of range Всплывающий индекс вне диапазона
