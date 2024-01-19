# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

# file = open(path, 'a', encoding='UTF-8')
# file - имя переменной
# open - что делаем с файлом
# path - путь к файлу (относительный или абсолютный)
# 'a' - флаг, с которым работаем (чтение, дополнение, перезапись) - read, append, write
# encoding='UTF-8' - кодировка, лучше всегда ее указывать

file = open('numbers.txt', 'a', encoding='UTF-8')
file.write(input("Введите строку для записи: ") + '\n')
file.close()


file = open('numbers.txt', 'w', encoding='UTF-8')   # w - перезаписывает файл
file.write(input("Введите строку для записи: ") + '\n')
file.close()

with open ('numbers.txt', 'w', encoding='UTF-8') as file:
    file.write(input("Введите строку для записи: ") + '\n')
    file.close()