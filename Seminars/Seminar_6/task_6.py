# Добавьте в модуль с загадками функцию, которая
# принимает на вход строку (текст загадки) и число (номер
# попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах
# отгадывания.
# Для хранения используйте защищённый словарь уровня
# модуля.
# Отдельно напишите функцию, которая выводит результаты
# угадывания из защищённого словаря в удобном для чтения
# виде.
# Для формирования результатов используйте генераторное
# выражение.
from task_4 import puzzle
from task_5 import puzzle_solut
from random import choice, randint
__dict_protect__ = {}
def puzzle_count(guess_text: str, guess_try: int):
    __dict_protect__[guess_text] = guess_try

def puzzle_count_print():
    for guess_text, guess_try in __dict_protect__.items():
        print(f'Загадку {guess_text} угадали c {guess_try} попытки')
print(puzzle_solut(5))
print(puzzle_count_print())
