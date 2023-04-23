"""
4. Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение.
Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией. Для создания списков
использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение. Вызвать вторую функцию.
В нее должна передаваться ссылка на созданный файл. Во второй функции необходимо реализовать открытие
файла и простой построчный вывод содержимого. Вся программа должна запускаться по вызову первой функции.
"""
import os
import random
import string


def create_file(file_name):
    if os.path.isfile(file_name):
        return f'Файл {file_name} уже существует'

    with open(file_name, 'w') as file:
        text_list = [''.join(random.choices(string.ascii_letters, k=random.randint(1, 10))) for _ in range(10)]
        numbers_list = [random.randint(0, 100) for _ in range(10)]
        file.writelines([f'{text} {number}\n' for text, number in zip(text_list, numbers_list)])
        return file


def print_file(file):
    with open(file.name, 'r') as f:
        for line in f:
            print(line)


print_file(create_file('task.txt'))
