# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# - декораторами для сохранения параметров,
# - декоратором контроля значений и
# - декоратором для многократного запуска.
# Выберите верный порядок декораторов.

def deco_with_params(count: int):
    result = []
    def outer(func):
        def inner(*args, **kwargs):
            for _ in range(count):
                result.append(func(*args, **kwargs))
            return result

        return inner

    return outer


@deco_with_params(5)
def simple_func(message: str):
    return message


print(simple_func('Привет'))
