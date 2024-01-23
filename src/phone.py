from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, count_sim):
        super().__init__(name, price, quantity)
        self._count_sim = count_sim

    @property
    def cnt_sim(self):
        return self._cnt_sim

    def cnt_sim(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Значение должно быть цифрой")
        self._cnt_sim = value

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__class__.__name__ + f"('{self.name}', {self.price}, {self.quantity}, {self._count_sim})"

