# Напишите программу, которая получает целое число и возвращает его 
# шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата

HEX_SYSTEM = 16

number: int = int(input("Введите число: "))

def transfer_to_the_system(number: int, HEX_SYSTEM: int) -> str:
    result: str = ' '

    while number != 0:
        mod: str = str(number % HEX_SYSTEM)
        result = mod + result
        number //= HEX_SYSTEM

    return result

selection: int = HEX_SYSTEM
transfer: str = transfer_to_the_system(number, selection)

print(f'Результат: {transfer}')
print(f'\nЧисло в шестнадцатиричной системе счисления: {hex(number)}')
