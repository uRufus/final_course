"""
6. Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport
на два класса. Инициализировать классы необязательно. Внутри каждого поместить функцию get_info, которая в
первом классе будет отвечать за вывод названия товара, а вторая — его цены.
реализовать выполнение каждой из функции тремя способами.
"""


class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def change_price(self, new_price):
        self.__price = new_price


class ItemDiscountReportName(ItemDiscount):

    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.__name = name
        self.__price = price - price / 100 * discount

    def get_info(self):
        print(f"{self.__name}")

    def get_parent_data(self):
        print(f"Товар {self.__name} стоит {self.__price} руб.")


class ItemDiscountReportPrice(ItemDiscount):

    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.__name = name
        self.__price = price - price / 100 * discount

    def get_info(self):
        print(f"{self.__price} руб.")

    def get_parent_data(self):
        print(f"Товар {self.__name} стоит {self.__price} руб.")


item = ItemDiscountReportName("Goods1", 100, 20)
item_2 = ItemDiscountReportPrice("Goods1", 100, 20)

# Вариант 1
item.get_info()
item_2.get_info()

# Вариант 2
for i in [item, item_2]:
    i.get_info()


# Вариант 3
def obj_handler(obj):
    obj.get_info()


for i in [item, item_2]:
    obj_handler(i)

