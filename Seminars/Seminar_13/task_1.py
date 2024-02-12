"""
Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или
вещественное число.
Обрабатывайте не числовые данные как исключения.
"""


def input_numeric():
    while True:
        data = ''
        try:
            data = input('Введите число: ')
            return int(data)
        except ValueError:
            try:
                return float(data)
            except ValueError as exc:
                print('Нужно ввести int или float: ' + exc.__class__.__name__)


number = input_numeric()
print(number)
