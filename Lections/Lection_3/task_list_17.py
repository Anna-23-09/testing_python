import copy

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_m = matrix.copy()
print(matrix, new_m, sep='\n')
matrix[0][1] = 555 # 555 добавится и в new_m
print(matrix, new_m, sep='\n') 


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_m = copy.deepcopy(matrix)
print(matrix, new_m, sep='\n')
matrix[0][1] = 555 # 555 НЕ БУДЕТ добавлена в new_m
print(matrix, new_m, sep='\n')
