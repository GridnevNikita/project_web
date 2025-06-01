import re
from collections import Counter
from typing import Any, Dict, List

import pytest

from src.filters import count_by_category, filter_by_description

test_transactions = [
    {
        "id": 1,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    },
    {
        "id": 2,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 3,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 4,
        "state": "EXECUTED",
        "date": "2018-07-11T02:26:18.671407",
        "operationAmount": {"amount": "79931.03", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Открытие вклада",
        "to": "Счет 72082042523231456215",
    },
]


def test_filter_by_description():
    # Фильтрация по ключевому слову "перевод"
    filtered = filter_by_description(test_transactions, "перевод")
    assert len(filtered) == 3
    assert all("перевод" in tx["description"].lower() for tx in filtered)


def test_count_by_category():
    categories = ["Перевод организации", "Перевод со счета на счет", "Открытие вклада", "Перевод с карты на карту"]
    counts = count_by_category(test_transactions, categories)
    expected = {
        "Перевод организации": 1,
        "Перевод со счета на счет": 1,
        "Открытие вклада": 1,
        "Перевод с карты на карту": 1,
    }
    assert counts == expected
