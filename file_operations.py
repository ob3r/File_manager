import os
import shutil
from config import WORKING_DIRECTORY
from modules.navigation import current_directory

def create_file(filename):
    """Создать файл в текущей директории"""
    filepath = os.path.join(current_directory, filename)
    with open(filepath, 'w') as f:
        pass
    return f"File {filename} created."

def read_file(filename):
    """Прочитать содержимое файла в текущей директории"""
    filepath = os.path.join(current_directory, filename)
    if os.path.isfile(filepath):
        with open(filepath, 'r') as f:
            return f.read()
    else:
        return "File does not exist."

def write_file(filename, content):
    """Записать содержимое в файл в текущей директории"""
    filepath = os.path.join(current_directory, filename)
    with open(filepath, 'w') as f:
        f.write(content)
    return f"Content written to {filename}."

def delete_file(filename):
    """Удалить файл в текущей директории"""
    filepath = os.path.join(current_directory, filename)
    if os.path.isfile(filepath):
        os.remove(filepath)
        return f"File {filename} deleted."
    else:
        return "File does not exist."

def copy_file(src, dest):
    """Скопировать файл в текущей директории"""
    src_path = os.path.join(current_directory, src)
    dest_path = os.path.join(current_directory, dest)
    if os.path.isfile(src_path):
        shutil.copy(src_path, dest_path)
        return f"File {src} copied to {dest}."
    else:
        return "Source file does not exist."

def move_file(src, dest):
    """Переместить файл в текущей директории"""
    src_path = os.path.join(current_directory, src)
    dest_path = os.path.join(current_directory, dest)
    if os.path.isfile(src_path):
        shutil.move(src_path, dest_path)
        return f"File {src} moved to {dest}."
    else:
        return "Source file does not exist."

def rename_file(src, dest):
    """Переименовать файл в текущей директории"""
    src_path = os.path.join(current_directory, src)
    dest_path = os.path.join(current_directory, dest)
    if os.path.isfile(src_path):
        os.rename(src_path, dest_path)
        return f"File {src} renamed to {dest}."
    else:
        return "Source file does not exist."
