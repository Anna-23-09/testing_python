text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'
with open('new_data.txt', 'a', encoding='utf-8') as f:
    res = f.write(text) # показывает, сколько байт информации было потрачено для переменной text
    print(f'{res = }\n{len(text) = }')
