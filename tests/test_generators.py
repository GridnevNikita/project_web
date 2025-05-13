import pytest

from src.generators import filter_by_currency

@pytest.fixture()
def filter_test_transactions():
    return [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {
                    "amount": "79114.93",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188"
            },
            {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {
                    "amount": "43318.34",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160"
            },
            {
                "id": 895315941,
                "state": "EXECUTED",
                "date": "2018-08-19T04:27:37.904916",
                "operationAmount": {
                    "amount": "56883.54",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229"
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
                "operationAmount": {
                    "amount": "67314.70",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Visa Platinum 1246377376343588",
                "to": "Счет 14211924144426031657"
            }
        ]


def test_filter_by_currency_usd(filter_test_transactions):
    # Успешная фильтрация по USD
    filtered_transactions = filter_by_currency(filter_test_transactions, "USD")

    # Проверяем первую транзакцию
    first_transaction = next(filtered_transactions)
    assert first_transaction == filter_test_transactions[0]

    # Проверяем вторую транзакцию
    second_transaction = next(filtered_transactions)
    assert second_transaction == filter_test_transactions[1]

    # Проверяем третью транзакцию
    third_transaction = next(filtered_transactions)
    assert third_transaction == filter_test_transactions[3]

    # Проверяем отсутствие дополнительных транзакций
    with pytest.raises(StopIteration):
        next(filtered_transactions)

    # Проверяем общее количество USD транзакций
    assert sum(1 for _ in filter_by_currency(filter_test_transactions, "USD")) == 3


def test_filter_by_currency_non_existing(filter_test_transactions):
    # Фильтрация по несуществующей валюте
    filtered_transactions = filter_by_currency(filter_test_transactions, "EUR")
    with pytest.raises(StopIteration):
        next(filtered_transactions)


def test_filter_by_currency_empty_list():
    # Фильтрация пустого списка
    empty_list = []
    filtered_transactions = filter_by_currency(empty_list, "USD")
    with pytest.raises(StopIteration):
        next(filtered_transactions)
