# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант.

things = {'палатка': 5, 'спальник': 2, 'фонарик': 1, 'еда': 2, 'вода': 3}
max_weight = 10

def backpack(things, max_weight):
    things_taken = []
    for things, weight in things.items():
        if weight <= max_weight:
            things_taken.append(things)
            max_weight -= weight
    return things_taken

print(backpack(things, max_weight))
