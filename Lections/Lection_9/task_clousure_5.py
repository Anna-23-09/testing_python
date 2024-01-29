from typing import Callable


def add_one_str(a: str) -> Callable[[str], str]:
    names = []

    def add_two_str(b: str) -> str:
        names.append(b)
        return a + ', ' + ', '.join(names)

    return add_two_str


hello = add_one_str('Hello')
bye = add_one_str('Good bye')

print(hello('Alex'))    # Hello, Alex
print(hello('Karina'))  # Hello, Alex, Karina
print(bye('Alina'))     # Good bye, Alina
print(hello('John'))    # Hello, Alex, Karina, John
print(bye('Neo'))       # Good bye, Alina, Neo
