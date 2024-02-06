# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.

class Archive:
    instance = None
    archive = []

    def __new__(cls, digit, letter):
        instance = super().__new__(cls)
        instance.digit = digit
        instance.letter = letter
        instance.archive = cls.archive.copy()
        # cls.instance = instance
        cls.archive.append(instance)
        return instance

    def __str__(self):  # представление для пользователя
        return f'Объект Архив ({self.digit}, {self.letter}) Архив: {self.archive}'

    def __repr__(self):  # представление для программиста
        return f'{self.digit}{self.letter}'


a = Archive(1, 'A')
b = Archive(2, 'B')
c = Archive(3, 'C')
d = Archive(4, 'D')

print(a)
print(a.archive)
print(b)
print(b.archive)
print(c)
print(c.archive)
print(d)
print(d.archive)
