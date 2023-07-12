def func(positional_only_parameters, /, positional_or_keyword_parameters, *, keyword_only_parameters):
    pass


def standart_argument(arg):
    # пример обычной функции
    print(arg)


standart_argument(42)
standart_argument(arg=42)
