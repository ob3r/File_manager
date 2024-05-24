import os
from config import WORKING_DIRECTORY
from modules.navigation import current_directory

def create_directory(dirname):
    """Создать директорию в текущей директории"""
    dirpath = os.path.join(current_directory, dirname)
    os.makedirs(dirpath, exist_ok=True)
    return f"Директория {dirname} создана."

def delete_directory(dirname):
    """Удалить директорию в текущей директории"""
    dirpath = os.path.join(current_directory, dirname)
    if os.path.isdir(dirpath):
        os.rmdir(dirpath)
        return f"Директория {dirname} удалена."
    else:
        return "Директории не существует."
