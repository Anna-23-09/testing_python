from sys import builtin_module_names, path # импортируем не весь модуль, а части builtin_module_names и path

print(builtin_module_names)
print(*path, sep='\n')
