# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

class Person:
    def __init__(self, name, surname, lastname, age):
        self.name = name
        self.surname = surname
        self.lastname = lastname
        self._age = age

    def birthday(self):
        self._age += 1

    def full_name(self):
        print(f'{self.surname} {self.name} {self.lastname}')

    def get_age(self):
        return self._age


a = Person('Анна', 'Толстова', 'Владимировна', 30)

print(a.full_name())
print(a.get_age())
a.birthday()
print(a.get_age())
