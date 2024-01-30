# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.

def deco_with_params(count: int):
    def outer(func):
        def inner(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)

        return inner

    return outer


@deco_with_params(3)
def simple_func(message: str):
    print(message)


simple_func('Привет')
