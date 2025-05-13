from datetime import datetime

import pytest

from src.processing import filter_by_state, sort_by_date


# Фикстура для filter_by_state
@pytest.fixture
def filter_test_data():
    return {
        "valid_data": [
            {"id": 1, "state": "EXECUTED", "date": "2023-01-01"},
            {"id": 2, "state": "CANCELED", "date": "2023-01-02"},
            {"id": 3, "state": "EXECUTED", "date": "2023-01-03"},
            {"id": 4, "state": "PENDING", "date": "2023-01-04"},
        ],
        "expected_result": [
            {"id": 1, "state": "EXECUTED", "date": "2023-01-01"},
            {"id": 3, "state": "EXECUTED", "date": "2023-01-03"},
        ],
        "invalid_data_type": "string",
        "missing_key_data": [{"id": 1, "date": "2023-01-01"}, {"id": 2}],
    }


# Фикстура для sort_by_date
@pytest.fixture
def sort_test_data():
    return {
        "valid_data": [
            {"id": 1, "date": "2023-01-01T00:00:00"},
            {"id": 2, "date": "2023-01-03T00:00:00"},
            {"id": 3, "date": "2023-01-02T00:00:00"},
        ],
        "expected_asc": [
            {"id": 1, "date": "2023-01-01T00:00:00"},
            {"id": 3, "date": "2023-01-02T00:00:00"},
            {"id": 2, "date": "2023-01-03T00:00:00"},
        ],
        "expected_desc": [
            {"id": 2, "date": "2023-01-03T00:00:00"},
            {"id": 3, "date": "2023-01-02T00:00:00"},
            {"id": 1, "date": "2023-01-01T00:00:00"},
        ],
        "invalid_data_type": "string",
        "missing_key_data": [{"id": 1}, {"date": "2023-01-01"}],
    }


# Тесты для filter_by_state
def test_filter_by_state_valid(filter_test_data):
    result = filter_by_state(filter_test_data["valid_data"])
    assert result == filter_test_data["expected_result"]


def test_filter_by_state_invalid_type(filter_test_data):
    with pytest.raises(TypeError):
        filter_by_state(filter_test_data["invalid_data_type"])


def test_filter_by_state_missing_key(filter_test_data):
    with pytest.raises(ValueError):
        filter_by_state(filter_test_data["missing_key_data"])


# Тесты для sort_by_date
def test_sort_by_date_valid(sort_test_data):
    result = sort_by_date(sort_test_data["valid_data"], reverse=False)

    # Проверяем каждую позицию отдельно
    assert len(result) == len(sort_test_data["expected_asc"])
    for i in range(len(result)):
        assert result[i]["date"] == sort_test_data["expected_asc"][i]["date"]
        assert result[i]["id"] == sort_test_data["expected_asc"][i]["id"]

    result = sort_by_date(sort_test_data["valid_data"])
    assert len(result) == len(sort_test_data["expected_desc"])
    for i in range(len(result)):
        assert result[i]["date"] == sort_test_data["expected_desc"][i]["date"]
        assert result[i]["id"] == sort_test_data["expected_desc"][i]["id"]


def test_sort_by_date_invalid_type(sort_test_data):
    with pytest.raises(TypeError):
        sort_by_date(sort_test_data["invalid_data_type"])


def test_sort_by_date_missing_key(sort_test_data):
    with pytest.raises(ValueError):
        sort_by_date(sort_test_data["missing_key_data"])
