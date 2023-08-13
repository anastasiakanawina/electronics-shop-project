from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        if not isinstance(other, Phone):
            raise ValueError('Складывать можно только объекты Item или Phone и дочерние от них.')
        return self.quantity + other.quantity

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if (number_of_sim <= 0) or ((number_of_sim * 10) % 10 > 0):
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        return self.__number_of_sim


