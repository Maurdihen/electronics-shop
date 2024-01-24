from src.item import Item


class MixinKeyboardChangeLan:
    def change_lang(self):
        if self._language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"

class Keyboard(Item, MixinKeyboardChangeLan):
    def __init__(self, name: str, price: float, quantity: int, language: str = "EN"):
        super().__init__(name, price, quantity)
        self._language = language


    @property
    def language(self):
        return self._language

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__class__.__name__ + f"('{self.name}', {self.price}, {self.quantity}, {self._language})"
