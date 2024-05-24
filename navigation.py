import os
from config import WORKING_DIRECTORY

current_directory = WORKING_DIRECTORY

def change_directory(path):
    """Изменить текущую директорию на указанную"""
    global current_directory
    new_path = os.path.abspath(os.path.join(current_directory, path))
    if new_path.startswith(WORKING_DIRECTORY):
        if os.path.isdir(new_path):
            current_directory = new_path
            return f"Директория изменена на {current_directory}"
        else:
            return "Директория не существует"
    else:
        return "Выход за пределы рабочей директории запрещен"

def list_directory():
    """Вывести список файлов и директорий текущей директории"""
    return os.listdir(current_directory)
