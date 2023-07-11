# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# 1) Какие вещи взяли все три друга
# 2) Какие вещи уникальны, есть только у одного друга
# 3) Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

friends = {
    'Anna': ('cat', 'cheese', 'hat', 'cream'),
    'Alex': ('boat', 'hat', 'coal', 'meat'),
    'Helen': ('cream', 'fish', 'boots', 'hat')
}

common_items = (
    set.union(set(friends['Anna']), set(friends['Alex']), set(friends['Helen'])))
print(common_items)

unique_items = set()

for item in friends.values():
    unique_items.update(set(item).difference(common_items))
print(unique_items)

