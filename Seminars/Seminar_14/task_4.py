"""
Напишите для задачи 1 тесты pytest. Проверьте следующие
варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""
import pytest
from task_1 import symbol_deleter


def test_no_change():
    assert (symbol_deleter('Something string') == 'something string')


def test_title():
    assert (symbol_deleter('SOMETHING STRING') == 'something string')


def test_punctuation():
    assert (symbol_deleter('Something! string?') == 'something string')


def test_foreign_letters():
    assert (symbol_deleter('Somethingсамсинг stringстринг') == 'something string')


def test_all():
    assert (symbol_deleter('ЫЩЬУЕРШТПSOMETHING!!! STRingСТРинг') == 'something string')


if __name__ == '__main__':
    pytest.main(['-v'])
