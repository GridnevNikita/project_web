import pytest

from src.masks import get_mask_account, get_mask_card_number


# Фикстуры для данных карт
@pytest.fixture
def card_data():
    return {
        "valid": "4000111122223333",
        "expected": "4000 11** **** 3333",
        "invalid": {
            "too_short": "123456789012345",
            "too_long": "12345678901234567",
            "with_letters": "123456789012345a",
            "integer": 12345678901234567,
            "empty": "",
            "special_chars": "123456789012345!",
        },
    }


# Фикстура для данных счетов
@pytest.fixture
def account_data():
    return {
        "valid": "40001111222233334444",
        "expected": "**4444",
        "invalid": {
            "too_short": "123456789012345",
            "too_long": "123456789012345678901",
            "with_letters": "123456789012345a",
            "integer": 12345678901234567890,
            "empty": "",
            "special_chars": "123456789012345!",
        },
    }


# Тесты для get_mask_card_number
def test_card_number_valid(card_data):
    result = get_mask_card_number(card_data["valid"])
    assert get_mask_card_number(card_data["valid"]) == card_data["expected"]
    assert len(result) == 19
    assert result.count(" ") == 3
    assert result[-4:].isdigit()


def test_card_number_invalid(card_data):
    for case, value in card_data["invalid"].items():
        with pytest.raises(Exception):
            get_mask_card_number(value)


# Тесты для get_mask_account
def test_account_number_valid(account_data):
    result = get_mask_account(account_data["valid"])
    assert result == account_data["expected"]
    assert len(result) == 6
    assert result.startswith("**")
    assert result[-4:].isdigit()


def test_account_number_invalid(account_data):
    for case, value in account_data["invalid"].items():
        with pytest.raises(Exception):
            get_mask_account(value)
