"""
Напишите для задачи 1 тесты unittest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""
import unittest
from task_1 import symbol_deleter


class TestSymbolDeleter(unittest.TestCase):

    def test_no_change(self):
        self.assertEqual(symbol_deleter('Something string'), 'something string')

    def test_change_title(self):
        self.assertEqual(symbol_deleter('SOMETHING STRING'), 'something string')

    def test_punctuation(self):
        self.assertEqual(symbol_deleter('SO?";METHI_NG STR&^%$ING'), 'something string')

    def test_foreign_letters(self):
        self.assertEqual('Somethingсамсинг stringстринг', 'something string')

    def test_all(self):
        self.assertEqual('ЫЩЬУЕРШТПSOMETHING!!! STRingСТРинг', 'something string')


if __name__ == '__main__':
    unittest.main(verbosity=2)
