from src.external_api import convert_to_rubles
import pytest
from unittest import mock


@mock.patch("src.external_api.requests.get")
def test_convert_usd_to_rub(mock_get):
    # Подготовка фиктивного ответа от API
    mock_get.return_value.status_code = 200
    mock_get.return_value.raise_for_status = mock.Mock()
    mock_get.return_value.json.return_value = {
        "rates": {
            "RUB": 100.0  # курс 1 USD = 100 рублей
        }
    }

    transaction = {
        "operationAmount": {
            "amount": "10.00",
            "currency": {
                "code": "USD"
            }
        }
    }

    result = convert_to_rubles(transaction)

    # Проверка результата: 10 * 100 = 1000
    assert result == 1000.0

    # Проверка правильности вызова requests.get
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/latest",
        headers={"apikey": mock.ANY},
        params={"base": "USD", "symbols": "RUB"}
    )


def test_convert_rub():
    transaction = {
        "operationAmount": {
            "amount": "1500.00",
            "currency": {
                "code": "RUB"
            }
        }
    }

    result = convert_to_rubles(transaction)
    assert result == 1500.0

def test_unsupported_currency():
    transaction = {
        "operationAmount": {
            "amount": "200.00",
            "currency": {
                "code": "GBP"
            }
        }
    }

    result = convert_to_rubles(transaction)
    assert result == 0.0

@mock.patch("src.external_api.requests.get")
def test_api_failure(mock_get):
    mock_get.side_effect = Exception("API error")

    transaction = {
        "operationAmount": {
            "amount": "20.00",
            "currency": {
                "code": "USD"
            }
        }
    }

    result = convert_to_rubles(transaction)
    assert result == 0.0

def test_missing_operation_amount():
    transaction = {
        "description": "Платёж без суммы"
    }

    result = convert_to_rubles(transaction)
    assert result == 0.0

def test_invalid_amount_value():
    transaction = {
        "operationAmount": {
            "amount": "abc",  # некорректное значение
            "currency": {"code": "RUB"}
        }
    }

    result = convert_to_rubles(transaction)
    assert result == 0.0

def test_operation_amount_is_none():
    transaction = {
        "operationAmount": None
    }

    result = convert_to_rubles(transaction)
    assert result == 0.0