# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, 
# а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

def make_dict(**kwargs):
    reverse_dict = dict()
    for key, value in kwargs.items():
        if isinstance(value, (list, dict, set)):
            value = str(value)
        reverse_dict[value] = key
    return reverse_dict


print(make_dict(students=["Jon", "Sara"], \
                     three_frends={1: "Boris", 2: "Gurgen", 3: "Bob"}))
