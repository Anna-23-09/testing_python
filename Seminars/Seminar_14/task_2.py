"""
Напишите для задачи 1 тесты doctest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""
import doctest
from string import ascii_lowercase

ascii_lowercase += ' '


def symbol_deleter(text):
    '''
    >>> symbol_deleter('Something string') == 'something string'
    True
    >>> symbol_deleter('SOMETHING STRING') == 'something string'
    True
    >>> symbol_deleter('Something! string?') == 'something string'
    True
    >>> symbol_deleter('Somethingсамсинг stringстринг') == 'something string'
    True
    >>> symbol_deleter('ЫЩЬУЕРШТПSOMETHING!!! STRingСТРинг') == 'something string'
    True
    '''
    if not isinstance(text, str):
        raise ValueError
    return ''.join([i.lower() for i in text if i.lower() in ascii_lowercase])


if __name__ == '__main__':
    doctest.testmod(verbose=True)
