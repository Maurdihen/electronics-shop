from src.item import Item
from src.keyboard import Keyboard
import pytest


class TestKeyboard:
    @pytest.fixture
    def keyboard(self):
        return Keyboard("Test Keyboard", 50.0, 2, "EN")

    def test_change_lang_switches_language_from_en_to_ru(self, keyboard):
        initial_language = keyboard.language
        keyboard.change_lang()
        assert keyboard.language == "RU"
        assert keyboard.language != initial_language

    def test_change_lang_switches_language_from_ru_to_en(self, keyboard):
        keyboard.change_lang()
        keyboard.change_lang()
        assert keyboard.language == "EN"

    def test_keyboard_str_method_returns_name(self, keyboard):
        expected_str = keyboard.name
        actual_str = str(keyboard)
        assert actual_str == expected_str

    def test_keyboard_repr_method_returns_correct_representation(self, keyboard):
        expected_repr = f"Keyboard('{keyboard.name}', {keyboard.price}, {keyboard.quantity}, {keyboard.language})"
        actual_repr = repr(keyboard)
        assert actual_repr == expected_repr
