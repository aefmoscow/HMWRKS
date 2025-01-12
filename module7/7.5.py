import os
import time

path = os.getcwd()
directory = '.'
# for dirpath, dirnames, filenames in os.walk(path):
#     print(dirpath, dirnames, filenames)
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        # parent_dir = root
        parent_dir = os.path.dirname(filepath)
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,'
            f' Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
