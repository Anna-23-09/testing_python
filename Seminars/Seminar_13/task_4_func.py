import json
from task_4_class import User


def create_user_list(path):
    result = set()
    with open(path, 'r', encoding='UTF-8') as data_file:
        data = json.load(data_file)
        for level, user in data.items:
            for id, name in user.items:
                result.add(User(name, id, level))
    return result
