# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)

import time


class MyString(str):
    def __new__(cls, value, author):
        instance = super(MyString, cls).__new__(cls, value)
        instance.author = author
        instance.creation_time = time.time()
        return instance

    # def __init__(self, value, author):
    #     super().__init__(value)
    #     self.author = author
    #     self.creation_time = time.time()


avtor: str = 'Anna'
my_string = MyString('плохой код', avtor)
print(my_string)
print(my_string.author)
print(my_string.creation_time)
