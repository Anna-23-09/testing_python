SIZE = 100
with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.read(SIZE): # прочитать файл не целиком, а порциями по 100 символов
        print(res)
