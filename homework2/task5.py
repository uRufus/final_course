"""
5. Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса
(метод init, в который должна передаваться переменная — скидка), и перегрузку метода str дочернего класса.
В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы
(вторая и третья строка после объявления дочернего класса).
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

    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.__name = name
        self.__price = price - price / 100 * discount

    def get_parent_data(self):
        print(f"Товар {self.__name} стоит {self.__price} руб.")


item = ItemDiscountReport("Goods1", 100, 20)

item.get_parent_data()
