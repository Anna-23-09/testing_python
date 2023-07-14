data = [2, 4, 6, 8, 10, ]
for item in data:
    print(item, end='\t') # вывод через Tab
print()


data = [2, 4, 6, 8, 10, ] 
print(*data, sep='\t') # то же самое, но короче
