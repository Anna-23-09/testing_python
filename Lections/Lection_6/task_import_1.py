import sys

print(sys)
print(sys.builtin_module_names)
print(*sys.path, sep='\n')

# содержимое переменной sys.path формируется динамически
# PYTHONPATH - переменная с путями до мест расположения модулей
# антипример:
# def randint(*args):
#     return 'Не то, что вы искали!' 
# 
# 
# 
# 
