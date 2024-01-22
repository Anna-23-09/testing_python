import json

my_dict = {
    "id": 123,
    "name": "Clementine Bauche",
    "username": "Cleba",
    "email": "cleba@corp.mail.ru",
    "address": {
        "street": "Central",
        "city": "Metropolis",
        "zipcode": "123456"
    },
    "phone": "+7-999-123-45-67"
}

res = json.dumps(my_dict, indent=2, separators=(',', ':'), sort_keys=True)  # отформатирует данный выше словарь my_dict
# убрали пробел после ",", убрали пробел после ":", включили сортировку ключей по алфавиту
# лучше разделители не менять ("," и ":")
print(res)
