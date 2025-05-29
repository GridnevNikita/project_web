from unittest.mock import patch

import pytest

from src.data_loader import csv_transactions, excel_transactions


@patch("src.data_loader.os.path.isfile")
@patch("src.data_loader.pd.read_csv")
def test_csv_transactions(mock_read_csv, mock_isfile):
    mock_isfile.return_value = True
    mock_read_csv.return_value.to_dict.return_value = [{"amount": 100, "category": "Food"}]

    result = csv_transactions("file.csv")
    assert result == [{"amount": 100, "category": "Food"}]
    mock_isfile.assert_called_once_with("file.csv")
    mock_read_csv.assert_called_once_with("file.csv", sep=";", encoding="utf-8")
    mock_read_csv.return_value.to_dict.assert_called_once_with(orient="records")


@patch("src.data_loader.os.path.isfile")
def test_csv_transactions_file_not_found(mock_isfile):
    mock_isfile.return_value = False

    with pytest.raises(FileNotFoundError, match="Файл не найден: missing.csv"):
        csv_transactions("missing.csv")

    mock_isfile.assert_called_once_with("missing.csv")


@patch("src.data_loader.os.path.isfile")
@patch("src.data_loader.pd.read_csv")
def test_csv_transactions_read_error(mock_read_csv, mock_isfile):
    mock_isfile.return_value = True
    mock_read_csv.side_effect = Exception("Ошибка чтения CSV")

    with pytest.raises(ValueError, match="Ошибка при чтении CSV-файла: Ошибка чтения CSV"):
        csv_transactions("bad.csv")

    mock_isfile.assert_called_once_with("bad.csv")
    mock_read_csv.assert_called_once_with("bad.csv", sep=";", encoding="utf-8")


@patch("src.data_loader.os.path.isfile")
@patch("src.data_loader.pd.read_excel")
def test_excel_transactions(mock_read_excel, mock_isfile):
    mock_isfile.return_value = True
    mock_read_excel.return_value.to_dict.return_value = [{"amount": 200, "category": "Transport"}]

    result = excel_transactions("file.xlsx")
    assert result == [{"amount": 200, "category": "Transport"}]
    mock_isfile.assert_called_once_with("file.xlsx")
    mock_read_excel.assert_called_once_with("file.xlsx")
    mock_read_excel.return_value.to_dict.assert_called_once_with(orient="records")


@patch("src.data_loader.os.path.isfile")
def test_excel_transactions_file_not_found(mock_isfile):
    mock_isfile.return_value = False

    with pytest.raises(FileNotFoundError, match="Файл не найден: missing.xlsx"):
        excel_transactions("missing.xlsx")

    mock_isfile.assert_called_once_with("missing.xlsx")


@patch("src.data_loader.os.path.isfile")
@patch("src.data_loader.pd.read_excel")
def test_excel_transactions_read_error(mock_read_excel, mock_isfile):
    mock_isfile.return_value = True
    mock_read_excel.side_effect = Exception("Ошибка чтения Excel")

    with pytest.raises(ValueError, match="Ошибка при чтении Excel-файла: Ошибка чтения Excel"):
        excel_transactions("bad.xlsx")

    mock_isfile.assert_called_once_with("bad.xlsx")
    mock_read_excel.assert_called_once_with("bad.xlsx")
