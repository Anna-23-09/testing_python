# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

# directory_path = r'D:\Аня\Geek Brains\Автотесты\Погружение в Python\testing_python\Seminars\Seminar_8'
from task_2_2 import load_json
import os
import json
import pickle
directory_path = r'D:\Аня\Geek Brains\Автотесты\Погружение в Python\testing_python\Seminars\Seminar_8'

def save_pickle(filename, data):
    with open(filename, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)


def search_json(dir_name: str):
    for obj in os.listdir(os.path.join(os.getcwd(), dir_name)):
        file_name, file_ext = obj.split('.')
        if file_ext == 'json':
            json_dict = load_json(obj)
            save_pickle(file_name + '.pickle', json_dict)


search_json(directory_path)
