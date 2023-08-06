import pytest
from src.item import Item


@pytest.fixture
def item_test():
    return Item("Смартфон", 10000, 20)


def test_price(item_test):
    """Когда мы создаем экземпляр класса со значениями ("Смартфон", 10000, 20),
        то calculate_total_price вернет 200000."""
    assert item_test.calculate_total_price() == 200000


def test_discount(item_test):
    """Когда мы создаем экземпляр класса со значениями ("Смартфон", 10000, 20),
        и скидкой в 20% то apply_discount вернет 8000.0."""
    Item.pay_rate = 0.8
    item_test.apply_discount()
    assert item_test.price == 8000.0

