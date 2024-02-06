# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При создании нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков архивов
# list-архивы также являются свойствами экземпляра

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

    def __repr__(self):
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
