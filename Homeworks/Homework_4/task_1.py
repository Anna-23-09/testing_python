# Напишите функцию для транспонирования матрицы


my_matrix = [[1, 2, 3], [11, 22, 33], [111, 222, 333], [4, 5, 6]]
#print(my_matrix)

trans_matrix = [[0 for j in range(len(my_matrix))] for i in range(len(my_matrix))]
#print(trans_matrix)

for i in range(len(my_matrix)):
    for j in range(len(my_matrix[0])):
        trans_matrix[j][i] = my_matrix[i][j]

print(my_matrix)
print(trans_matrix)
