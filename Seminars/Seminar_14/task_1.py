"""
Создайте функцию, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.
"""

from string import ascii_lowercase

ascii_lowercase += ' '


def symbol_deleter(text):
    if not isinstance(text, str):
        raise ValueError
    return ''.join([i.lower() for i in text if i.lower() in ascii_lowercase])


if __name__ == '__main__':
    print(symbol_deleter('vdhafh фщцушгещ 5987вдяалпо elенkiop'))
