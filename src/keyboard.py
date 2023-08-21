from src.item import Item
from src.mixin_ch_lang import LanguageMixin


class Keyboard(Item, LanguageMixin):
    """ Класс для товара Клавиатура """

    def __init__(self, name, price, quantity, language="EN"):
        super().__init__(name, price, quantity)
        self.__language = "EN"
        LanguageMixin.__init__(self, language)
