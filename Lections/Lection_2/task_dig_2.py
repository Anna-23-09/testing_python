import sys

STEP = 2 ** 16
num = 1
for _ in range(30): # используем _, если переменная не нужна. В последовательности из 30, делаем 30 итераций
    print(sys.getsizeof(num), num)
    num *= STEP
