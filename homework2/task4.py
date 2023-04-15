"""
4. Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский,
и дочерний классы получили новое значение цены. Следует проверить это, вызвав соответствующий метод родительского класса
 и функцию дочернего (функция, отвечающая за отображение информации о товаре в одной строке).
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


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        print(f"Товар {self.get_name()} стоит {self.get_price()} руб.")


item = ItemDiscountReport("Goods1", 100)
item.change_price(200)

item.get_parent_data()
print(item.get_price())
