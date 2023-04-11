"""
2. Дополнить следующую функцию недостающим кодом:
def print_directory_contents(sPath):
Функция принимает имя каталога и распечатывает его содержимое
в виде «путь и имя файла», а также любые другие
файлы во вложенных каталогах.

Эта функция подобна os.walk. Использовать функцию os.walk
нельзя. Данная задача показывает ваше умение работать с
вложенными структурами.
"""
import os
from pathlib import Path


def print_directory_contents(sPath):
    files_list = os.listdir(sPath)
    if len(files_list) > 0:
        for v in files_list:
            print(f"{sPath}\\{v}")
            if os.path.isdir(f"{sPath}\\{v}"):
                print_directory_contents(f"{sPath}\\{v}")


print_directory_contents(Path("..\\"))
