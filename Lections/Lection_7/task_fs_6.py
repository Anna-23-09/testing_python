"""Добавляем файлы в каталоги для демонстрацмм"""
import shutil   # позволяет проводить масштабные манипуляции

shutil.rmtree('dir/other_dir')  # удаляем только other_dir с содержимым
shutil.rmtree('some_dir')   # удаляем всю some_dir
