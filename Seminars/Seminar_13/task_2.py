"""
Создайте функцию аналог get для словаря.
Помимо самого словаря функция принимает ключ и
значение по умолчанию.
При обращении к несуществующему ключу функция должна
возвращать дефолтное значение.
Реализуйте работу через обработку исключений.
"""

def dict_get(my_dict, my_key, default_value):
    try:
        return my_dict[my_key]
    except KeyError as e:
        return default_value


dict1 = {1: 'one', 2: 'two'}

print(dict_get(dict1, 1, '0'))
print(dict_get(dict1, 3, '0'))
