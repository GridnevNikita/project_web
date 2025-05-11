import pytest

from src.widget import get_date, mask_account_card


# Фикстура для mask_account_card
@pytest.fixture
def mask_data():
    return {
        "valid": {
            "card": "Maestro 1596837868705199",
            "account": "Счет 64686473678894779589",
            "expected_card": "Maestro 1596 83** **** 5199",
            "expected_account": "Счет **9589",
        },
        "invalid": {
            "empty": "",
            "not_string": 1234567890,
            "wrong_format": "1234567890123456",
            "missing_type": "1596837868705199",
        },
    }


# Фикстура для get_date
@pytest.fixture
def date_data():
    return {
        "valid": {"date_string": "2024-12-11T02:26:18.671407", "expected": "11.12.2024"},
        "invalid": {"empty": "", "wrong_format": "11122024", "not_string": 20241211, "incomplete": "2024-12"},
    }


# Тесты для mask_account_card
# Тесты для mask_account_card
def test_mask_account_card_valid(mask_data):
    assert mask_account_card(mask_data["valid"]["card"]) == mask_data["valid"]["expected_card"]
    assert mask_account_card(mask_data["valid"]["account"]) == mask_data["valid"]["expected_account"]


def test_mask_account_card_invalid(mask_data):
    with pytest.raises(ValueError):
        mask_account_card(mask_data["invalid"]["empty"])
    with pytest.raises(TypeError):
        mask_account_card(mask_data["invalid"]["not_string"])
    with pytest.raises(ValueError):
        mask_account_card(mask_data["invalid"]["wrong_format"])
    with pytest.raises(ValueError):
        mask_account_card(mask_data["invalid"]["missing_type"])


# Тесты для get_date
def test_get_date_valid(date_data):
    assert get_date(date_data["valid"]["date_string"]) == date_data["valid"]["expected"]


def test_get_date_invalid(date_data):
    with pytest.raises(ValueError):
        get_date(date_data["invalid"]["empty"])
    with pytest.raises(TypeError):  # Для целых чисел
        get_date(date_data["invalid"]["not_string"])
    with pytest.raises(ValueError):  # Для неверного формата
        get_date(date_data["invalid"]["wrong_format"])
    with pytest.raises(ValueError):  # Для неполной даты
        get_date(date_data["invalid"]["incomplete"])
