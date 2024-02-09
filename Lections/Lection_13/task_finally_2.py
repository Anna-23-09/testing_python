file = open('text.txt', 'r', encoding='UTF-8')
try:
    data = file.read().split()
    print(data[len(data)])
finally:
    print('Закрываю файл')
    file.close()
