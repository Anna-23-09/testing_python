# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

my_list = [3, 7, 1, 98, 23, 16, 0, -4]
print(my_list)


def func(my_list):
    for j in range(len(my_list) - 1):
        for i in range(len(my_list) - 1 - j):
            if my_list[i] > my_list[i+1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    return my_list


print(func(my_list))
