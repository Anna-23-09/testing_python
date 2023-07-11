# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

list = [6, 2, 6, 4, 3, 11, 45, 27, 11, 0, 0, 11, 43, 32, 98]
TWO = 2

for element in set(list):
    if list.count(element) == TWO:
        for _ in range(TWO):
            list.remove(element)
print(list)
            