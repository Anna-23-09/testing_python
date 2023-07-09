# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение дробей. 
# Для проверки своего кода используйте модуль fractions

fraction_1: str = str(input("Введите дробь вида 'a/b': "))
fraction_2: str = str(input("Введите дробь вида 'a/b': "))

def result (fraction_1, fraction_2):
    num1, denom1 = map(int, fraction_1.split("/"))
    num2, denom2 = map(int, fraction_2.split("/"))

    sum_frac_num = num1 * denom2 + num2 * denom1
    sum_frac_denom = denom1 * denom2
    sum_frac = (sum_frac_num, sum_frac_denom)

    prod_frac_num = num1 * num2
    prod_frac_denom = denom1 * denom2
    prod_frac = (prod_frac_num, prod_frac_denom)

    return sum_frac, prod_frac

sum_frac, prod_frac = result(fraction_1, fraction_2)

print(f"Сумма дробей {fraction_1} и {fraction_2} - {sum_frac[0]}/{sum_frac[1]}")
print(f"Произведение дробей {fraction_1} и {fraction_2} - {prod_frac[0]}/{prod_frac[1]}")

