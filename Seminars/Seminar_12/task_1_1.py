class Factorial:
    def __init__(self, limit: int):
        self.limit = limit
        self.result = []

    def __call__(self, count: int):
        fact = 1
        list_fact = []
        for i in range(1, self.limit):
            fact *= i
            list_fact.append(fact)

        self.result.append(list_fact[-self.limit:])
        return fact


a = Factorial(3)

print(a(10))
print(a.result)
