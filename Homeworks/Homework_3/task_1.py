# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

my_list = ['cat', 'dog', 'cat', 'hat', 'ball', 'cat', 'ball', 'pen', 'cat']

list_with_dublicate = []

for item in my_list:
    if my_list.count(item) > 1 and item not in list_with_dublicate:
        list_with_dublicate.append(item)
print(list_with_dublicate) # Вернуть список с дублирующимися элементами. 



new_list = set(my_list)
print(new_list) # В результирующем списке не должно быть дубликатов.
