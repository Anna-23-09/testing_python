# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.

text = "jkljjjjllk"
my_dict = {}

for letter in text:
    if letter not in my_dict:
        my_dict[letter] = 1
    else:
        my_dict[letter] += 1
print(my_dict)

new_dict = {}
for letter in set(text):
    new_dict[letter] = text.count(letter)
print(new_dict)
