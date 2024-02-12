"""
Создайте класс с базовым исключением и дочерние классы исключения:
○ ошибка уровня,
○ ошибка доступа.
"""


class MyError(Exception):
    def __init__(self, msg, message):
        self.message = message
        self.msg = msg

    def __str__(self):
        return f'{self.msg}: {self.message}'


class LevelError(MyError):
    def __init__(self, message):
        super().__init__('Ошибка уровня', message)


class AccessError(MyError):
    def __init__(self, message):
        super().__init__('Ошибка доступа', message)

if __name__ == '__main__':
    raise AccessError('Не хватает прав')


# raise AccessError('Не хватает прав')
raise LevelError(7)
