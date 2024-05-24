import navigation, file_operations, directory_operations, help


def main():
    print("File Manager")
    while True:
        command = input(f"{navigation.current_directory}> ").strip().split()
        if not command:
            continue

        cmd, *args = command
        if cmd == "cd":
            # Переход в директорию
            if args:
                print(navigation.change_directory(args[0]))
            else:
                print("Usage: cd <directory>")
        elif cmd == "ls":
            # Вывод списка файлов и директорий
            print(navigation.list_directory())
        elif cmd == "mkfile":
            # Создание файла
            if args:
                print(file_operations.create_file(args[0]))
            else:
                print("Usage: mkfile <filename>")
        elif cmd == "read":
            # Чтение файла
            if args:
                print(file_operations.read_file(args[0]))
            else:
                print("Usage: read <filename>")
        elif cmd == "write":
            # Запись в файл
            if len(args) >= 2:
                print(file_operations.write_file(args[0], ' '.join(args[1:])))
            else:
                print("Usage: write <filename> <content>")
        elif cmd == "rmfile":
            # Удаление файла
            if args:
                print(file_operations.delete_file(args[0]))
            else:
                print("Usage: rmfile <filename>")
        elif cmd == "cp":
            # Копирование файла
            if len(args) == 2:
                print(file_operations.copy_file(args[0], args[1]))
            else:
                print("Usage: cp <source> <destination>")
        elif cmd == "mv":
            # Перемещение файла
            if len(args) == 2:
                print(file_operations.move_file(args[0], args[1]))
            else:
                print("Usage: mv <source> <destination>")
        elif cmd == "rename":
            # Переименование файла
            if len(args) == 2:
                print(file_operations.rename_file(args[0], args[1]))
            else:
                print("Usage: rename <source> <destination>")
        elif cmd == "mkdir":
            # Создание директории
            if args:
                print(directory_operations.create_directory(args[0]))
            else:
                print("Usage: mkdir <directory>")
        elif cmd == "rmdir":
            # Удаление директории
            if args:
                print(directory_operations.delete_directory(args[0]))
            else:
                print(f"Usage: rmdir <directory>")
        elif cmd == "exit":
            # Выход из программы
            break
        elif cmd == "help":
            # Вывод справки
            help.help()
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
