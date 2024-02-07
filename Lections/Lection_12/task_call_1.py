class Number:
    def __init__(self, num):
        self.num = num


n = Number(42)
print(f'{callable(Number) = }')     # True
print(f'{callable(n)      = }')     # False
