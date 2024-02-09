def get(text: str = None) -> int:
    data = input(text)
    try:
        num = int(data)     # SyntaxError: expected 'except' or 'finally' block
    return num


if __name__ == '__main__':
    number = get('Введите целый делитель: ')
    print(f'100 / {number} = {100 / number}')

