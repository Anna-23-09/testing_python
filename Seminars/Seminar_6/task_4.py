# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными
# вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была
# отгадана загадка или ноль, если попытки исчерпаны.

def puzzle(puzzle_text: str, variant: list[str], tries: int) -> int:
    print(puzzle_text)
    variant_v = list(map(lambda x: x.lower(), variant))
    num = 0
    while num < tries:
        user_input = input("Введите ответ: ").lower()
        if user_input in variant_v:
            num += 1
            return num
        else:
            print("Ошибочка")


