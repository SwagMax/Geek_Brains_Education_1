"""
4. *(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов
строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы
фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие
записи, в которых фамилия начинается с соответствующей буквы. Например:

#>>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "И": {
        "И": ["Илья Иванов"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
    "А": ["Анна Савельева"]
    }
}

Как поступить, если потребуется сортировка по ключам?
"""


def thesaurus_adv(name):
    name_dict = {}
    for i in name:
        name_dict.setdefault(i.split()[-1][0], {}).setdefault(i[0], []).append(i)
    return name_dict


name = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"]
print(thesaurus_adv(name))

