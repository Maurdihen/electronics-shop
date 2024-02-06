from unittest.mock import patch, mock_open

import pytest

import src
from src.exceptions import PhoneException, InstantiateCSVError
from src.item import Item

class TestItemClass:

    @pytest.fixture
    def sample_item(self):
        return Item("Test Item", 10.0, 5)

    def test_item_initialization(self, sample_item):
        assert sample_item.name == "Test Item"
        assert sample_item.price == 10.0
        assert sample_item.quantity == 5

    def test_calculate_total_price(self, sample_item):
        assert sample_item.calculate_total_price() == 50.0

    def test_apply_discount(self, sample_item):
        sample_item.pay_rate = 0.8
        sample_item.apply_discount()
        assert sample_item.price == 8.0

    def test_name_property(self, sample_item):
        sample_item.name = "New Test Item Name"
        assert sample_item.name == "New Test I"

    @staticmethod
    def generate_csv_data(items):
        return "\n".join([f"{item['name']},{item['price']},{item['quantity']}" for item in items])

    def test_instantiate_from_csv_success(self, tmp_path):
        items_data = [
            {"name": "Item1", "price": "10.0", "quantity": "3"},
            {"name": "Item2", "price": "15.0", "quantity": "2"}
        ]

        csv_data = self.generate_csv_data(items_data)
        csv_file_path = tmp_path / "test_items.csv"

        with open(csv_file_path, "w") as csv_file:
            csv_file.write(csv_data)

        with patch("builtins.open", mock_open(read_data=csv_data)) as mock_file:
            items = Item.instantiate_from_csv(csv_file_path)

        assert len(items.all) == 2
        assert items.all[0].name == "Item1"
        assert items.all[1].quantity == 2

    def test_instantiate_from_csv_file_not_found(self, tmp_path):
        csv_file_path = tmp_path / "non_existent_file.csv"

        with pytest.raises(FileNotFoundError, match="Отсутствует файл item.csv"):
            Item.instantiate_from_csv(csv_file_path)

    def test_instantiate_from_csv_key_error(self):
        with pytest.raises(FileNotFoundError):
            Item.instantiate_from_csv("../src/item.csv")

        # with pytest.raises(InstantiateCSVError):
        #     Item.instantiate_from_csv("../src/items.csv")

    def test_string_to_number(self):
        assert Item.string_to_number("10") == 10
        assert Item.string_to_number("15.5") == 15
        assert Item.string_to_number("20.0") == 20

    def test_add_items(self):
        item1 = Item("Item1", 10.0, 3)
        item2 = Item("Item2", 15.0, 2)

        result = item1 + item2
        assert result == 5

    def test_add_items_error(self):
        item1 = Item("Item1", 10.0, 3)
        with pytest.raises(PhoneException):
            result = item1 + "invalid_item"
