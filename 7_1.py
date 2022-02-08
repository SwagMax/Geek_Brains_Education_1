'''1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
    |--my_project
        |--settings
        |--mainapp
        |--adminapp
        |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как
лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена
папок под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить
данные о вложенных папках и файлах (добавлять детали)?'''

import os

path_root = r'C:\Users\Администратор\ProjectGB\Geek_Brains_Education_1'
main_folder = 'my_project'
folders = ['settings', 'mainapp', 'adminapp', 'authapp']

path_root_main_folder = os.path.join(path_root, main_folder)
if not os.path.exists(path_root_main_folder):
    os.mkdir(path_root_main_folder)

for _ in folders:
    path_folder = os.path.join(path_root_main_folder, _)
    if not os.path.exists(path_folder):
        os.mkdir(path_folder)