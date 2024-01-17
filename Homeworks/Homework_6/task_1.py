#Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
# На вход будет подаваться дата в формате "день.месяц.год".
# Ваша задача - создать программу, которая проверяет, является ли введенная дата корректной или нет.
# Ваша программа должна предоставить ответ "True" (дата корректна)
# или "False" (дата некорректна) в зависимости от результата проверки.

def my_date(date: str):
    day, month, year = list(map(int, date_to_prove.split('.')))
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if not (1 <= day <= 31):
            return False
    elif month in [4, 6, 9, 11]:
        if not (1 <= day <= 30):
            return False
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            if not (1 <= day <= 29):
                return False
        else:
            if not (1 <= day <= 28):
                return False
    else:
        return False

    if not (1 <= month <= 12):
        return False

    if year <= 0:
        return False

    return True


date_to_prove = input()
print(my_date(date_to_prove))