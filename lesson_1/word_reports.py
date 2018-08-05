import os
import collections

from lesson_1.utils.check_words import get_top_verbs_in_path


projects = [
    'django',
    'flask',
    'pyramid',
    'reddit',
    'requests',
    'sqlalchemy',
]


def get_projects_verbs():
    """

    :return: список глаголов в проектах
    """
    verbs = []
    for project in projects:
        project_path = os.path.join('.', project)
        print(project_path)
        verbs += get_top_verbs_in_path(project_path)
    return verbs


def verb_report(_top_size=200):
    """

    :param _top_size:
    :return: Выводит отчет по глаголам
    """
    verbs = get_projects_verbs()
    print('total %s verbs, %s unique' % (len(verbs), len(set(verbs))))
    for word, occurence in collections.Counter(verbs).most_common(_top_size):
        print(word, occurence)


verb_report()
