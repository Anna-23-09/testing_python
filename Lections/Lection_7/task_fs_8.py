import os
from pathlib import Path

print(os.listdir())  # получаем список всех файлов и каталогов в cwd

p = Path(Path().cwd())
for obj in p.iterdir():
    print(obj)  # получаем путь для каждого файла и директории
