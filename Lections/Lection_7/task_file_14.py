with open('text_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')
        # считать файл. Каждый раз считывая строку, сохраняем ее в переменную line и выводим на печать
