from typing import Any, Dict

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def filter_test_data() -> Dict[str, Any]:
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


@pytest.fixture
def sort_test_data() -> Dict[str, Any]:
    return {
        "valid_data": [
            {"id": 1, "date": "2023-01-01T00:00:00.000000"},
            {"id": 2, "date": "2023-01-03T00:00:00.000000"},
            {"id": 3, "date": "2023-01-02T00:00:00.000000"},
        ],
        "expected_asc": [
            {"id": 1, "date": "2023-01-01T00:00:00.000000"},
            {"id": 3, "date": "2023-01-02T00:00:00.000000"},
            {"id": 2, "date": "2023-01-03T00:00:00.000000"},
        ],
        "expected_desc": [
            {"id": 2, "date": "2023-01-03T00:00:00.000000"},
            {"id": 3, "date": "2023-01-02T00:00:00.000000"},
            {"id": 1, "date": "2023-01-01T00:00:00.000000"},
        ],
        "invalid_data_type": "string",
        "missing_key_data": [{"id": 1}, {"date": "2023-01-01T00:00:00.000000"}],
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

    assert result == sort_test_data["expected_asc"]

    result = sort_by_date(sort_test_data["valid_data"])
    assert result == sort_test_data["expected_desc"]


def test_sort_by_date_invalid_type(sort_test_data):
    with pytest.raises(TypeError):
        sort_by_date(sort_test_data["invalid_data_type"])


def test_sort_by_date_missing_key(sort_test_data):
    with pytest.raises(ValueError):
        sort_by_date(sort_test_data["missing_key_data"])
