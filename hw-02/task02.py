# Реализуйте класс товар, в который включите свойства и методы общие для любого товара из магазина бытовой электроники
# (не менее двух свойств и методов).

# Реализуйте двух наследников товара, например, классы телевизор и холодильник,
# которые должны будут иметь в дополнение к наследуемым хотя бы по одному собственному уникальному свойству и методу.

# Пополните ассортимент своего виртуального магазина несколькими разными товарами с различными параметрами.

# Рассчитайте среднюю цену всех созданных товаров, используя главный класс.

# Реализуйте корректное сравнение двух товаров между собой по их исключительному свойству,
# например, два объекта-телевизора будут считаться равными между собой, если у них одинаковая диагональ.

# Сравните несколько товаров между собой.


class Product:
    """properties and methods for any household appliance product"""
    list_of_products = []

    def __init__(self, price, power):
        self.price = price  # for the 1 unit
        self.power = power
        Product.list_of_products.append(self.price)

    def info(self):
        """Return the good's basis info"""
        return print('The price of this model is', self.price, "rubles, and it's power is", self.power, 'kW')

    def ecology(self):
        """Shows how much electricity the product consumes per day"""

        return print('It consumes ', self.power*24, ' kW per day ')

    @staticmethod
    # avg_price
    def func():
        return print("Average price is", sum(Product.list_of_products) / len(Product.list_of_products))


class TV(Product):

    def __init__(self, price, power, screen_size, frequency):
        super().__init__(price, power)
        self.screen_size = screen_size
        self.frequency = frequency

    def gaming(self):
        return self.frequency >= 120

    def __eq__(self, other):
        # comparison TV sizes
        if isinstance(other, TV):
            return self.screen_size == other.screen_size
        return NotImplemented


class Refrigerator(Product):
    def __init__(self, price, power, defrosting, freezer):
        super().__init__(price, power)
        self.defrosting = defrosting
        self.freezer = freezer

    def ice_cream(self):
        if self.freezer:
            return print("Yes, you can store an ice cream here")
        else:
            return print("So sorry, but you can't store ice cream here :(")

    def __eq__(self, other):
        # comparison capability ice cream storage
        if isinstance(other, Refrigerator):
            return self.ice_cream() == other.ice_cream()
        return NotImplemented


samsung_tv = TV(67000, 0.25, 50, 60)
lg_tv = TV(10000, 0.15, 50, 120)
indesit_ref = Refrigerator(25000, 0.3, 'Non frost', True)
bosch_ref = Refrigerator(35000, 0.5, 'Frost', False)

print(Product.func())
print(samsung_tv == lg_tv)
print(indesit_ref == bosch_ref)
