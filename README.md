# Файловый Менеджер

Этот проект представляет собой простой файловый менеджер для командной строки, написанный на Python. Он предоставляет базовые функции для навигации по файловой системе и выполнения операций с файлами и директориями.

## Функции

- Изменить текущую директорию (`cd`)
- Показать содержимое текущей директории (`ls`)
- Создать новый файл (`mkfile`)
- Прочитать содержимое файла (`read`)
- Записать содержимое в файл (`write`)
- Удалить файл (`rmfile`)
- Скопировать файл (`cp`)
- Переместить файл (`mv`)
- Переименовать файл (`rename`)
- Создать новую директорию (`mkdir`)
- Удалить директорию (`rmdir`)

## Использование

Файловый менеджер запускается с помощью скрипта `file_manager.py`. Он выводит приветственное сообщение, а затем ожидает ввода пользователя. Ввод должен быть командой, за которой следуют ее аргументы, разделенные пробелами.

Например, чтобы изменить текущую директорию на поддиректорию с именем `subdir`, вы должны ввести `cd subdir`.

Чтобы показать содержимое текущей директории, вы должны ввести `ls`.

Чтобы создать новый файл с именем `file.txt`, вы должны ввести `mkfile file.txt`.

И так далее для других команд.

## Модули

Проект организован в несколько модулей:

- `navigation.py`: Содержит функции для навигации по файловой системе.
- `file_operations.py`: Содержит функции для выполнения операций с файлами.
- `directory_operations.py`: Содержит функции для выполнения операций с директориями.
- `config.py`: Содержит настройки конфигурации для файлового менеджера.

## Конфигурация

Рабочая директория для файлового менеджера указывается в файле `config.py`. По умолчанию он установлен на `C:\Users\Admin\PycharmProjects\File_manager`. Вы можете изменить его на любую директорию в вашей системе.
