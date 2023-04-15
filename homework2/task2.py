"""
2. Инкапсулировать оба параметра (название и цену) товара родительского класса.
Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.
"""


class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        print(f"Товар {self.__name} стоит {self.__price} руб.")


item = ItemDiscountReport("Goods1", 100)
item.get_parent_data()
