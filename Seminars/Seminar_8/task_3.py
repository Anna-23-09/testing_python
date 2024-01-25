# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.
import json
import csv

def json_to_csv(filename: str):
    with open(filename, 'r', encoding='UTF-8') as file:
        json_dict = json.load(file)


    user_list = []
    for u_lvl, user in json_dict.items():
        for u_id, u_name in user.items():
            user_list.append((u_name, u_id, u_lvl))

    with open(filename.split('.')[0] + '.csv', 'w', encoding='UTF-8') as csv_file:
        csv_write = csv.writer(csv_file, dialect='excel', delimiter='|', lineterminator='\n')
        csv_write.writerow(['Имя', 'ID', 'level'])
        for row in user_list:
            csv_write.writerow(row)


json_to_csv('test/workers.json')
