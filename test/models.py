class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """

        if self.quantity >= quantity:
            return True
        else:
            return False


    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """

        if Product.check_quantity(self, quantity):
            return True
        else:
            raise ValueError('продуктов не хватает')




    def __hash__(self):
        return hash(self.name + self.description)


class Cart:

    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if buy_count <= 0:
            raise ValueError("Количество должно быть положительным")
        elif product in self.products:
            self.products[product] += buy_count
            return buy_count
        else:
            self.products[product] = buy_count
            return buy_count


    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if product in self.products.keys():
            if remove_count is None or remove_count >= self.products[product]:
                self.products.pop(product)
            else:
                self.products[product] -= remove_count
            return self.products[product]
        else:
            raise KeyError("Cart clear")

    def clear(self):
        return self.products.clear()

    def get_total_price(self) -> float:
        total_sum = 0.0
        for product, quantity in self.products.items():
            total_sum += product.price * quantity
        return total_sum

    def buy(self, cash_client : float = 400.0):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """

        """
        Ниже закомментировал переменную которую ввожу из консоли, думал добавить интерактива, 
        но работает только если запускать тесты через консоль pytest -s test/test_shop.py
        Оставлю переменную, с ней метод тоже работает, 
        но чтобы тест запускался через интерфейс введу статичную
        """

        #cash_client = float(input("Enter your quantity money: "))
        if cash_client >= self.get_total_price():
            for product in self.products.keys():
                product.buy(quantity=self.products[product])
            self.clear()
        else:
            raise ValueError('Dont have cash')



# -------------For test-------------
item_for_product = Product("book", 100, "This is a book", 1000)
# item_for_product.buy(100)
item_for_cart = Cart()
item_for_cart.get_total_price()
item_for_cart.add_product(item_for_product, 4)
item_for_cart.buy()
# item_for_cart.remove_product(item_for_product, 4)
item_for_cart.add_product(item_for_product, 3)
# item_for_cart.clear()

