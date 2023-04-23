"""
5. Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке часть
строковых значений заменить на значения типа example345 (строка+число). Далее — усовершенствовать вторую
функцию из предыдущего примера (функцию извлечения данных). Дополнительно реализовать поиск определенных
подстрок в файле по следующим условиям: вывод первого вхождения, вывод всех вхождений.
Реализовать замену всех найденных подстрок на новое значение и вывод всех подстрок,
состоящих из букв и цифр и имеющих пробелы только в начале и конце — например, example345.
"""

import os
import random
import re
import string


def create_file(file_name):
    if os.path.isfile(file_name):
        return f'Файл {file_name} уже существует'

    with open(file_name, 'w') as file:
        text_list = [''.join(random.choices(string.ascii_letters, k=random.randint(1, 10))) for _ in range(100)]
        new_text_list = []
        for text in text_list:
            new_text_list.append(f"{text}{''.join(random.choices(string.digits, k=random.randint(1, 10)))}")
        numbers_list = [random.randint(0, 100) for _ in range(100)]
        file.writelines([f'{text} {number}\n' for text, number in zip(new_text_list, numbers_list)])
        return file


def print_file(file):
    f_r = open('replace.txt', 'w')
    with open(file.name, 'r') as f:
        for line in f:
            # вывод первого вхождения
            find_single = re.search(r"c", line)
            if find_single:
                print(find_single.group(0))
            else:
                print(None)

            # вывод всех вхождений
            find_all = re.findall(r'B', line)
            print(find_all)

            # вывод всех подстрок, состоящих из букв и цифр и имеющих пробелы только
            # в начале и конце — например, example345.
            no_spaces = re.match(r'^[A-z0-9]*', line)
            print(no_spaces.group(0))

            # Замена значений на test
            text_number = re.match(r'\w*', line)
            line = line.replace(text_number.group(0), 'test')
            print(line)
            f_r.write(line)

        f_r.close()


print_file(create_file('task.txt'))
