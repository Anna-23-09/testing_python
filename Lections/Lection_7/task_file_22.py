text = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        'Ut enim ad minim veniam, quis nostrud exercitation ullamco',
        'Duis aute irure dolor in reprehenderit in voluptate velit esse cillu', ]
with open('new_data.txt', 'w', encoding='utf-8') as f:
    print(f.tell()) # выводим файл new_data (пока пустой)
    for line in text:
        f.write(f'{line}\n')    # добавляем символ переноса в конце файла
        print(f.tell())
    print(f.tell())
print(f.tell())  # ValueError: I/O operation on closed file.
