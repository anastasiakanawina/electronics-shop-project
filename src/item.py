import csv
from src.instantiate_csv_error import InstantiateCSVError

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = int(str(price).replace('_', ''))
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f'{self.__name}'

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item или Phone и дочерние от них.')
        return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        """
        Rласс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """
        cls.all.clear()
        try:
            with open('../src/items.csv', newline='', encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                if reader.fieldnames != ['name', 'price', 'quantity']:
                    raise InstantiateCSVError()
                else:
                    for row in reader:
                        cls(row['name'], row['price'], row['quantity'])
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")


    @staticmethod
    def string_to_number(string):
        return int(float(string))
