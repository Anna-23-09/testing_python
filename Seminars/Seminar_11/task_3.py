# Добавьте к задачам 1 и 2 строки документации для классов.

class Archive:
    """
    Мой класс создает объекты архива, которые хранят в себе число и строку
    """
    instance = None
    archive = []

    def __new__(cls, digit, letter):
        """
        Создает новый объект
        :param digit: - целое число
        :param letter: - строка с 1 буквой
        """
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
print(help(Archive))    # вызываем документацию класса Archive
