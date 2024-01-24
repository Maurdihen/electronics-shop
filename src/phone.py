from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Значение должно быть положительной цифрой")
        self._number_of_sim = value

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__class__.__name__ + f"('{self.name}', {self.price}, {self.quantity}, {self._number_of_sim})"

