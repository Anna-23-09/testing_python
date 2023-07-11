# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в верхнем регистре в остальных случаях
def task():
    current_text: str = input('Введите строку: \n')

    if current_text.isdigit():
        return int(current_text)
    elif current_text.replace('.', '', 1).isdigit():
        return float(current_text)
    elif current_text[0] == '-' and current_text.replace('-', '', 1).replace('.', '', 1).isdigit():
        return float(current_text)
    elif current_text.lower() != current_text:
        return current_text.lower
    else:
        return current_text.upper()

print(task())
