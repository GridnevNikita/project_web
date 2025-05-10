import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "card_number,expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567890123456", "1234 56** **** 3456"),
        ("4321098765432109", "4321 09** **** 2109"),
        ("9876543210987654", "9876 54** **** 7654"),
    ],
)
def test_card_number_parametrized(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number,expected",
    [
        ("73654108430135874305", "**4305"),  # Базовый случай
        ("12345678901234567890", "**7890"),  # Другой валидный номер
        ("09876543210987654321", "**4321"),  # Обратный порядок цифр
        ("98765432109876543210", "**3210"),  # Еще один валидный номер
    ],
)
def test_account_number_parametrized(account_number, expected):
    assert get_mask_account(account_number) == expected


# Проверка ошибок для card_number
def test_card_number_type_error():
    with pytest.raises(TypeError):
        get_mask_card_number(1234567890123456)
    with pytest.raises(TypeError):
        get_mask_card_number(["1234567890123456"])
    with pytest.raises(TypeError):
        get_mask_card_number({"card": "1234567890123456"})


def test_card_number_empty():
    with pytest.raises(ValueError):
        get_mask_card_number("")


# Проверка ошибок для account_number
def test_account_number_type_error():
    with pytest.raises(TypeError):
        get_mask_account(12345678901234567890)
    with pytest.raises(TypeError):
        get_mask_account(["12345678901234567890"])
    with pytest.raises(TypeError):
        get_mask_account({"account": "12345678901234567890"})


def test_account_number_empty():
    with pytest.raises(ValueError):
        get_mask_account("")
