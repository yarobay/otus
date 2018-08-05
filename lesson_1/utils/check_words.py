import ast
import collections
from lesson_1.utils.list_utils import flat
from lesson_1.utils.file_tree import get_trees

import nltk
nltk.download('averaged_perceptron_tagger')


def is_verb(_word):
    """
    Проверяет входящее слово. Глагол или нет
    :param _word:
    :return:
    """
    if not _word:
        return False
    pos_info = nltk.pos_tag([_word])
    return pos_info[0][1] == 'VB'


def get_all_names(tree):
    """

    :param tree:
    :return: Список всех слов дерева
    """
    return [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]


def get_verbs_from_function_name(function_name):
    """

    :param function_name:
    :return: Список глаголов в названии функций
    """
    return [_word for _word in function_name.split('_') if is_verb(_word)]


def get_all_words_in_path(_path):
    """

    :param _path: путь до дирректории с файлами
    :return: Список всех слов в названиях фалов в дирректории
    """
    trees = [t for t in get_trees(_path) if t]
    words = [f for f in flat([get_all_names(t) for t in trees]) if
             not (f.startswith('__') and f.endswith('__'))]

    return flat([_word.split('_') for _word in words])


def get_top_verbs_in_path(_path, _top_size=10):
    trees = [t for t in get_trees(_path) if t]
    fncs = [f for f in
            flat([[node.name.lower() for node in ast.walk(t) if isinstance(node, ast.FunctionDef)] for t in trees]) if
            not (f.startswith('__') and f.endswith('__'))]
    print('functions extracted')
    verbs = flat([get_verbs_from_function_name(function_name) for function_name in fncs])
    return collections.Counter(verbs).most_common(_top_size)


def get_top_functions_names_in_path(_path, _top_size=10):
    trees = get_trees(_path)
    names = [fnc for fnc in
             flat([[node.name.lower() for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)] for tree in
                   trees]) if
             not (fnc.startswith('__') and fnc.endswith('__'))]
    return collections.Counter(names).most_common(_top_size)