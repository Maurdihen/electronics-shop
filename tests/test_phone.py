import pytest

from src.item import Item
from src.phone import Phone

from src.exceptions import PhoneException


class TestPhoneClass:
    def test_creating_phone_object(self) -> None:
        phone1 = Phone('test', 1, 2, 3)
        assert phone1.__dict__ == {'_name': 'test', 'price': 1, 'quantity': 2, '_count_sim': 3}

    def test_adding_phone_objects(self):
        phone1 = Phone('test', 1, 2, 3)
        phone2 = Phone('test1', 1, 2, 3)
        item1 = Item('test3', 1, 3)
        assert phone1 + phone2 == 4
        assert phone1 + item1 == 5

    def test_add_phone_exception(self):
        with pytest.raises(PhoneException):
            phone1 = Phone('test1', 1, 2, 3)
            return phone1 + 2

    def test_cnt_sim_valid_input(self):
        phone = Phone('test', 1, 2, 3)
        phone.cnt_sim(2)
        assert phone._cnt_sim == 2

    def test_cnt_sim_invalid_input(self):
        phone = Phone('test', 1, 2, 3)
        with pytest.raises(ValueError, match="Значение должно быть цифрой"):
            phone.cnt_sim("invalid")

    def test_add_valid_inputs(self):
        phone1 = Phone('test', 1, 2, 3)
        phone1.quantity = 3
        phone2 = Phone('test', 1, 2, 3)
        phone2.quantity = 4
        result = phone1 + phone2
        assert result == 7
