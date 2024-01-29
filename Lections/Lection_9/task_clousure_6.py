from typing import Callable


def add_one_str(a: str) -> Callable[[str], str]:
    text = ''   # str - НЕизменяемый тип, поэтому нужна строка 8 ( параметр nonlocal)

    def add_two_str(b: str) -> str:
        nonlocal text   # нужен этот параметр, т к str - НЕизменяемый тип
        # чтобы не перепутать можно его указать даже для изменяемых типов, код не испортится
        text += ', ' + b
        return a + text

    return add_two_str


hello = add_one_str('Hello')
bye = add_one_str('Good bye')

print(hello('Alex'))    # Hello, Alex
print(hello('Karina'))  # Hello, Alex, Karina
print(bye('Alina'))     # Good bye, Alina
print(hello('John'))    # Hello, Alex, Karina, John
print(bye('Neo'))       # Good bye, Alina, Neo
