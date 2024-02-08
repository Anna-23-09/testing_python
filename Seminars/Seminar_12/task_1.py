# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.

class FactorialCalculator:
    def __init__(self, k=5):
        self.k = k
        self.history = {}

    def calc_factorial(self, n):
        result = 1
        for i in range(1, n +1):
            result *= i
        self.history[n] = result
        return result

    def get_history(self):
        return self.history


fc = FactorialCalculator(k=3)
print(fc.calc_factorial(3))
print(fc.calc_factorial(5))
print(fc.calc_factorial(2))
print(fc.history)
