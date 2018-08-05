import os
import ast


def fill_file_list(_path):
    """

    :param _path: путь до директории с файлами
    :return: список всех фалйлов с расширением '.py'
    """
    file_list = []
    for dir_name, dirs, files in os.walk(_path, topdown=True):
        # file_list = [os.path.join(dir_name, file) for file in files if file.endswith('.py')]
        for file in files:
            if file.endswith('.py'):
                file_list.append(os.path.join(dir_name, file))
            if len(file_list) == 100:
                break
    print('total %s files' % len(file_list))
    return file_list


def get_trees(_path, with_file_names=False, with_file_content=False):
    """

    :param _path: путь до дирректории
    :param with_file_names: включть имена файлов в список или нет
    :param with_file_content: включть контент файлов в список или нет
    :return: Список (дерево)
    """
    trees = []
    file_names = fill_file_list(_path)
    for file in file_names:
        with open(file, 'r', encoding='utf-8') as attempt_handler:
            main_file_content = attempt_handler.read()
        try:
            tree = ast.parse(main_file_content)
        except SyntaxError as e:
            print(e)
            tree = None
        if with_file_names and with_file_content:
            trees.append((file, main_file_content, tree))
        elif with_file_names and not with_file_content:
            trees.append((file, tree))
        else:
            trees.append(tree)
    print('trees generated')
    return trees
