import os
from pathlib import Path

# os.rmdir('dir')    # OSError нужно указать путь
# Path('some_dir').rmdir()    # OSError нужно указать путь
os.rmdir('dir/other_dir/new_os_dir')    # удаляем new/os/dir
Path('some_dir/dir/new_path_dir').rmdir()

# rm - remove = удалить
