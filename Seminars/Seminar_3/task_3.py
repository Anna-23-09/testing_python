# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

my_tuple = (2, 'Anna', 4.02, [3, 5, 2], False, 89-23)
print(my_tuple)
my_dict = {}

for item in my_tuple:
    k = my_dict.setdefault(type(item).__name__, [])
    k.append(item)

print(my_dict)
