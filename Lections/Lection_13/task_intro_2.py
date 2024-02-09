def get(text: str = None) -> int:
    data = input(text)
    num = int(data)
    return num


if __name__ == '__main__':
    number = get('Введите целый делитель: ')
    print(f'{number} = {100 / number}')
