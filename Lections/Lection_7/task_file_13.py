SIZE = 100
with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.readline(SIZE): # когда строка короче 100 символов, считываем строку от начала до конца
        # и прекращаем чтение
        print(res)
