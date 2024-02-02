# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# шестизначный идентификационный номер
# уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь


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
class Worker(Person):
    def __init__(self, name, surname, lastname, age: int):
        super().__init__(name, surname, lastname, age)
        self.id_worker = __import__('random').randint(100000, 999999)
        self.access = sum(map(int, str (self.id_worker))) % 7


a = Worker('Анна', 'Толстова', 'Владимировна', 30)

print(a.id_worker)
print(a.access)
