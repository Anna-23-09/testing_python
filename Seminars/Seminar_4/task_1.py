# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.

def task_1(current_txt: str):
    list_work = current_txt.split()
    list_work.sort()
    max_len = 0

    for item in list_work:
        if max_len < len(item):
            max_len = len(item)

    for i, item in enumerate(list_work, start=1):
        print(f'{i}. {item:>{max_len}}')

txt = 'самые мягкие лапки'
task_1(txt)
