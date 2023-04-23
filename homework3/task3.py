"""
3. Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и значений словарь.
Если ключу не хватает значения, в словаре для него должно сохраняться значение None.
Значения, которым не хватило ключей, необходимо отбросить.
"""


def create_dict(keys, values):
    new_dict = {}
    for i in range(len(keys)):
        try:
            new_dict[keys[i]] = values[i]
        except IndexError:
            new_dict[keys[i]] = None

    return new_dict


first_list = ['a', 'b', 'c']
second_list = [1, 2, 3, 4, 5]
third_list = [1, 2]

print(create_dict(first_list, second_list))
print(create_dict(first_list, third_list))
