import csv

from src.exceptions import PhoneException


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self._name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self) -> None:
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, data_name):
        self._name = data_name[0:10]

    @classmethod
    def instantiate_from_csv(cls, path):
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(string):
        try:
            return int(string)
        except:
            return int(float(string))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        raise PhoneException(f"Невозможно сложить {self.__class__} с {other.__class__}")