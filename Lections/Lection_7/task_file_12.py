with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.readline: # после каждой строки получаем пустую строку
        print(res)
