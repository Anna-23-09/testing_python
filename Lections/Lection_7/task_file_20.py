text = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        'Ut enim ad minim veniam, quis nostrud exercitation ullamco',
        'Duis aute irure dolor in reprehenderit in voluptate velit esse cillu', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        print(line, file=f) # вывести информацию не в консоль, а в файловый дескриптор
