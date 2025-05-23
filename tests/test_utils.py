from unittest import mock
import json
from src.utils import load_json_file

@mock.patch('builtins.open', side_effect=FileNotFoundError)
def test_file_not_found(mock_open):
    result = load_json_file('fake_path.json')
    assert result == []

@mock.patch('json.load', side_effect=json.JSONDecodeError("Expecting value", "", 0))
@mock.patch('os.path.isfile', return_value=True)  # чтобы обойти проверку isfile
def test_json_decode_error(mock_isfile, mock_json_load):
    result = load_json_file('fake_path.json')
    assert result == []

@mock.patch('json.load', return_value={"not": "a list"})
@mock.patch('os.path.isfile', return_value=True)
def test_not_a_list(mock_isfile, mock_json_load):
    result = load_json_file('fake_path.json')
    assert result == []

@mock.patch("os.path.isfile", return_value=True)
@mock.patch("builtins.open", new_callable=mock.mock_open, read_data='[{"id": 1}, {"id": 2}]')
@mock.patch("json.load", return_value=[{"id": 1}, {"id": 2}])
def test_valid_json_list(mock_json_load, mock_open, mock_isfile):
    result = load_json_file("fake_path.json")
    assert result == [{"id": 1}, {"id": 2}]
