#✔ Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
#✔ Используйте комплексные числа
# для извлечения квадратного корня.

a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))

d = b ** 2 - 4 * a * c
result = ''

if d > 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    result = f'\n Уравнение имеет 2 вещественных корня: {(x1, x2)}'

elif d == 0:
    x = -b / (2 * a)
    result = f'\n Уравнение имеет 1 вещественный корень: {x}'

else:
    d = complex(d, 0)
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    result = f'\n Уравнение имеет 2 комплексных корня: {(x1, x2)}'

print(result)
