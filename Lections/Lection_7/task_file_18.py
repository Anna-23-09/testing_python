text = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        'Ut enim ad minim veniam, quis nostrud exercitation ullamco',
        'Duis aute irure dolor in reprehenderit in voluptate velit esse cillu', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        res = f.write(f'{line}\n')  # добавляем перенос на новую строку для удобочитаемости
        print(f'{res = }\n{len(line) = }')
