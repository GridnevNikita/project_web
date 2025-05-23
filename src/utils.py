import json
import os
from typing import Any, List


def load_json_file(file_path: str) -> List[Any]:
    """
    Загружает и возвращает список из JSON-файла.
    Возвращает пустой список, если файл не существует, не читается,
    или содержимое не является списком.
    """
    if not os.path.isfile(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


if __name__ == "__main__":
    transactions = load_json_file("../data/operations.json")
    print(transactions)
