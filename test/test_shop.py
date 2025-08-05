"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture(scope='function', autouse=True)
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False
        assert product.check_quantity(0) is True
        assert product.check_quantity(500) is True
        assert product.check_quantity(999) is True
        assert product.check_quantity(10000) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(1000) is True
        assert product.buy(500) is True
        assert product.check_quantity(1001) is False

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError) as error:
            product.buy(1050)
            assert 'продуктов не хватает' in str(error)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """


    def test_add_product_cart_negative(self, buy_count = -100):
        product = Product("book", 100, "This is a book", 1000)
        unit = Cart()
        with pytest.raises(ValueError) as error:
            unit.add_product(product, buy_count)
            assert "Количество должно быть положительным" in str(error)


    def test_add_product_cart_positive(self, buy_count = 2):
        product = Product("book", 100, "This is a book", 1000)
        unit = Cart()
        assert unit.add_product(product, buy_count) == 2


    def test_remove_product_cart(self, remove_count = 3):
        product = Product("book", 100, "This is a book", 1000)
        unit = Cart()
        unit.add_product(product, 5)
        assert unit.remove_product(product, remove_count) == 2


    def test_clear_all_cart(self):
        product = Product("book", 100, "This is a book", 1000)
        unit = Cart()
        unit.add_product(product, 5)
        assert unit.clear() is None


    def test_get_total_sum_cart(self):
        product = Product("book", 100, "This is a book", 1000)
        unit = Cart()
        unit.add_product(product, 5)
        assert unit.get_total_price() == 500


    def test_buy_cart_positive(self):
        product = Product("book", 100, "This is a book", 1000)
        unit = Cart()
        unit.add_product(product, 3)
        assert unit.buy(cash_client = 400) is True

    def test_buy_cart_negative(self):
        product = Product("book", 100, "This is a book", 1000)
        unit = Cart()
        unit.add_product(product, 6)
        with pytest.raises(ValueError) as error:
            unit.buy(cash_client=599)
        assert "Dont have money bro" in str(error.value)


        product = Product("book", 100, "This is a book", 1)
        unit = Cart()
        unit.add_product(product, 3)
        with pytest.raises(ValueError) as error:
            unit.buy()
        assert f'Dont have {product.name}' in str(error)
