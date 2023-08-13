import pytest
from src.phone import Phone


@pytest.fixture
def phone_test():
    return Phone("Смартфон", 10000, 20, 2)


def test_add(phone_test):
    """ Тестирование магического метода repr """
    assert repr(phone_test) == "Phone('Смартфон', 10000, 20, 2)"


def test_number_of_sim(phone_test):
    """ Тестирование количества сим """
    with pytest.raises(ValueError):
        phone_test.number_of_sim = 0
        phone_test.number_of_sim = -1
        phone_test.number_of_sim = 1.4
