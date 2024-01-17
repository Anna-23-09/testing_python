size = 63
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    print(f.truncate(size))
