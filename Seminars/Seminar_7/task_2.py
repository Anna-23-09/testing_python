# Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
import random
from random import randint, choice

vowels = ['e', 'u', 'i', 'o', 'a']
consonant = ['q', 'w', 'r', 't', 'y', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']


def generate_name():
    MIN_NAME_LEN = 4
    MAX_NAME_LEN = 7
    name_len = randint(MIN_NAME_LEN, MAX_NAME_LEN)
    rand_name = ''
    is_vowels = False
    for i in range(name_len):
        dict_choice = randint(0, 1)
        if dict_choice:
            is_vowels = True
        rand_name += random.choice(vowels) if dict_choice else random.choice(consonant)

    if not is_vowels:
        rand_name += 'a'

    return rand_name.capitalize()


def write_names(count: int):
    with open('names.txt', 'a', encoding='UTF-8') as f:
        for _ in range(count):
            f.write(generate_name() + '\n')


write_names(10)
