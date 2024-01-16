# Добавьте в модуль с загадками функцию, которая хранит
# словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы
# передать ей все свои загадки.
import random
from task_4 import puzzle
from random import choice, randint
def puzzle_solut(count: 2):
    dict_puzzle = {
        "Зимой и летом одним цветом": ["ель", "пихта", "доллар"],
        "Висит груша нельзя скушать": ["лампа","лампочка"],
        "Не лает не кусает в дом не пускает":["замок","гусь"]
}
    count = count if count < len(dict_puzzle) else len(dict_puzzle)
    for _ in range(count):

        cur_puzzle = choice(list(dict_puzzle))
        cur_value = dict_puzzle.pop(cur_puzzle)
        res = puzzle(cur_puzzle, cur_value, randint(1,3))


print(puzzle_solut(5))