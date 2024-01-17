import os

for dir_path, dir_name, file_name in os.walk(os.getcwd()):
    print(f'{dir_path = }\n{dir_name = }\n{file_name =}')
# dir_pass - путь к cwd
# dir_name - список с названиями директорий внутри
# file_name - список файлов, которые лежат внутри
