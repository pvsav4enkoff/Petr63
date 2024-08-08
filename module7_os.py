import os
import time

dir_path = r"C:\1"
for root, dirs, files in os.walk(dir_path):
    for file in files:
        path = root + '/' + file
        filetime = time.strftime("%d.%m.%Y %H:%M", time.localtime(os.path.getmtime(path)))
        print(f"Обнаружен файл: {file}, Путь: {os.path.join(root, file)}, Размер: {os.path.getsize(path)} байт, "
              f"Время изменения: {filetime}, Родительская директория: {root}")
