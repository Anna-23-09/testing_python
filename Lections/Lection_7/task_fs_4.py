import os
from pathlib import Path

# os.makedirs('dir/other_dir/new_os_dir')
# Path('some_dir/dir/new_path_dir').mkdir()  # Error: Системе не удается найти указанный путь:
# 'some_dir\\dir\\new_path_dir'
Path('some_dir/dir/new_path_dir').mkdir(parents=True)   # Error: Невозможно создать файл,
# так как он уже существует: 'dir/other_dir/new_os_dir'
