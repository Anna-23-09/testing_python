last = before = 0
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
    print(f.seek(before, 0))  # переносим курсор в конец строки
    print(f.truncate())  # обрезаем по позиции курсора
