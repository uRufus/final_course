"""
3. Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации
(нуль необходимо исключить). Заполнить этими данными список и словарь.
Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
Вывести содержимое созданных списка и словаря.
"""
from pprint import pprint
from random import randint


def generator(a, b):
    # Проверям, что входные данные положительные
    if a <= 0:
        return f"{a} не положительное число"
    elif b <= 0:
        return f"{b} не положительное число"
    elif b <= a:
        return f" Число {b} должно быть больше числа {a}"

    gen_list = []
    gen_dict = {}

    # По второму числу бeрем длину массива
    for i in range(b):
        number = randint(a, b)
        gen_list.append(number)
        gen_dict[f"elem_{i + 1}"] = number
    return gen_list, gen_dict


# Запрашиваем ввод чисел
first_number = int(input("Введите первое положительное число: "))
second_number = int(input("Введите второе положительное число: "))

pprint(generator(first_number, second_number))
