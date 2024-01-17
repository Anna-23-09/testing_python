import os
from pathlib import Path

file_1 = os.path.join(os.getcwd(), 'dir', 'new_file.txt')  # в join передаем: в текущей рабочей директории (cwd)
# в dir файл new_file.txt
print(f'{file_1 = }\n{file_1}')  # укажет путь

file_2 = Path().cwd() / 'dir' / 'new_file.txt'
print(f'{file_2 = }\n{file_2}')
