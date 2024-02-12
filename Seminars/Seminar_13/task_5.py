"""
Доработаем задачи 3 и 4. Создайте класс проекта, который
имеет следующие методы:
загрузка данных (функция из задания 4)
вход в систему - требует указать имя и id пользователя. Для
проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из
множества пользователей.
добавление пользователя. Если уровень пользователя
меньше, чем ваш уровень, вызывайте исключение уровня
доступа.
"""

from task_4_func import create_user_list
from task_4_class import User
from task_3 import AccessError


class UserSystem:
    def __init__(self):
        self.access = False
        self.user_base = create_user_list('workers.json')
        self.authorized_user = None

    def login(self, login_user: User):
        if login_user in self.user_base:
            self.authorized_user = login_user
            return login_user.level
        else:
            raise AccessError('Пользователь с такими данными отсутствует в базе')


if __name__ == '__main__':
    our_system = UserSystem()
    user = User('Стоун', '2345')
    print(user)
