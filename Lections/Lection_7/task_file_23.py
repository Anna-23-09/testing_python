last = before = 0
text = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        'Ut enim ad minim veniam, quis nostrud exercitation ullamco',
        'Duis aute irure dolor in reprehenderit in voluptate velit esse cillu', ]
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():     # начинаем считывать строки
        last, before = f.tell(), last
        print(f'{last = }, {before = }')    # запись информации
    print(f'{last = }, {before = }')    # запись информации
    print(f'{f.seek(before, 0) = }')    # установить позицию в значении переменной before (134), начиная от начала файла (0)
    f.write('\n'.join(text))    # записываем новые строки кода
