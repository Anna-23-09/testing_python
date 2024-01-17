import os
from pathlib import Path

print(os.getcwd())
print(Path.cwd())
os.chdir('../..')   # меняем рабочую директорию на 2 ступени выше
print(os.getcwd())
print(Path.cwd())
