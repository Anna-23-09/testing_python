# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключом для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.

import json


def load_json(path: str) -> dict[int, dict[int, str]]:
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            return json.load(file)
    except:
        return {}


def save_json(path: str, data: dict[int, dict[int, str]]):
    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def enter_names():
    while name := input('Введите имя (ENTER для выхода): '):
        id_list = []
        user_data = load_json('test/workers.json')
        for user in user_data.values():
            for user_id in user:
                id_list.append(user_id)
        while True:
            user_id = input('Введите ID пользователя: ')
            if not user_id.isdigit():
                print('ID должен состоять из цифр! Повторите ввод!')
                continue
            if user_id not in id_list:
                break
            print(f'{user_id} такой ID уже зарегистрирован!')
        while True:
            user_lvl = input('Введите уровень доступа (1-7): ')
            if user_lvl.isdigit() and 0 < int(user_lvl) < 8:
                break
            print("Уровень доступа целое число от 1 до 7!")
        if user_lvl in user_data:
            user_data[user_lvl][user_id] = name
        else:
            user_data[user_lvl] = {user_id: name}
        save_json('test/workers.json', user_data)


if __name__ == '__main__':
    enter_names()
