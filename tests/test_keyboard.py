import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard_test():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_add():
    """ Тестирование метода change_lang """
    keyboard_test.change_lang()
    assert str(keyboard_test.language) == "RU"
