def from_one_to_n(n, data=[]):
    for i in range(1, n + 1):
        data.append(i)
    return data


new_list = from_one_to_n(5)
print(f'{new_list = }')
other_list = from_one_to_n(7) # список от 1 до 5 пополнится еще и от 1 до 7. Итого 12 элементов
print(f'{other_list = }') # это плохой способ
