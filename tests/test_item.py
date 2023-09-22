import pytest
from src.item import Item

@pytest.fixture
def sample_item():
    item = Item('Телефон', 10000, 5)
    yield item
    Item.all = []

def test_item_name_length(sample_item):
    # Проверяем, что длина наименования товара меньше 10 символов
    sample_item.name = 'Смартфон'
    assert sample_item.name == 'Смартфон'

def test_item_name_length_exception(sample_item):
    # Проверяем, что длина наименования товара больше 10 символов
    with pytest.raises(Exception, match="Длина наименования товара превышает 10 символов."):
        sample_item.name = 'СуперСмартфон'

def test_instantiate_from_csv():
    Item.instantiate_from_csv('test_items.csv')  # Создание объектов из тестового файла
    assert len(Item.all) == 5  # В файле 5 записей с данными по товарам

def test_item_name_after_csv_instantiation():
    Item.instantiate_from_csv('test_items.csv')  # Создание объектов из тестового файла
    item1 = Item.all[0]
    assert item1.name == 'СуперСмарт'

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

if __name__ == '__main__':
    pytest.main()
