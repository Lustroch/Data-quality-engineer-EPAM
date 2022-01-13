# Реализуйте класс товар, в который включите свойства и методы общие для любого товара из магазина бытовой электроники
# (не менее двух свойств и методов).

# Реализуйте двух наследников товара, например, классы телевизор и холодильник,
# которые должны будут иметь в дополнение к наследуемым хотя бы по одному собственному уникальному свойству и методу.

# Пополните ассортимент своего виртуального магазина несколькими разными товарами с различными параметрами.

# Рассчитайте среднюю цену всех созданных товаров, используя главный класс.

# Реализуйте корректное сравнение двух товаров между собой по их исключительному свойству,
# например, два объекта-телевизора будут считаться равными между собой, если у них одинаковая диагональ.

# Сравните несколько товаров между собой.


class Product(object):
    """properties and methods for any household appliance product"""
    list = []

    def __init__(self, price, number):
        self.price = price  # for the 1 unit
        self.number = number
        self.__class__.list.append(self.p)

    def info(self):
        """Return the good's basis info"""
        return self.p, self.n

    def cost(self, amount):
        """Cost per number of goods"""
        return self.p * amount

    @staticmethod
    # avg_price
    def func():
        return sum(Product.list) / len(Product.list)


class TV(Product):

    def __init__(self, price, number, screen_size, frequency):
        super().__init__(price, number)
        self.ss = screen_size
        self.freq = frequency

    def gaming(self):
        if self.freq >= 120:
            return True
        else:
            return False

    def __eq__(self, other):
        # comparesation TV sizes
        if isinstance(other, TV):
            return self.ss == other.ss
        return NotImplemented


class Refrigerator(Product):

    def __init__(self, price, number, defrosting, freezer):
        super().__init__(price, number)
        self.defr = defrosting
        self.fr = freezer

    def ice_cream(self):
        if self.fr:
            return True
        else:
            return False

    def __eq__(self, other):
        # comparison capability ice cream storage
        if isinstance(other, Refrigerator):
            return self.ice_cream() == other.ice_cream()
        return NotImplemented


samsung_tv = TV(67000, 6, 50, 60)
lg_tv = TV(10000, 10, 50, 120)
indesit_ref = Refrigerator(25000, 9, 'Non frost', True)
bosch_ref = Refrigerator(35000, 12, 'Frost', False)

print(Product.func())
print(samsung_tv == lg_tv)
print(indesit_ref == bosch_ref)
