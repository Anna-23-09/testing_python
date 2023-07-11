# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

txt: str = str(input("Введите строку: ")).split()

txt.sort()
max_len = 0

for item in txt:
    if len(item) > max_len:
        max_len = len(item)

for i, item in enumerate(txt, 1):
    print(f'{i}. {item:>{max_len}}')
