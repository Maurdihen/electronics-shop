from src.item import Item

from src.exceptions import PhoneException


class Phone(Item):
    def __init__(self, name, price, quantity, count_sim):
        super().__init__(name, price, quantity)
        self.count_sim = count_sim

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__class__.__name__ + f"('{self.name}', {self.price}, {self.quantity}, {self.count_sim})"

    def __add__(self, other):
        if isinstance(other, self.__class__) or issubclass(self.__class__, other.__class__):
            return self.quantity + other.quantity
        raise PhoneException(f"Невозможно сложить {self.__class__} с {other.__class__}1")
