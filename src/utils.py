import json
import logging
import os
from typing import Any, List

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "utils.log")
file_handler = logging.FileHandler(log_path, encoding="utf-8")

file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_json_file(file_path: str) -> List[Any]:
    """
    Загружает и возвращает список из JSON-файла.
    Возвращает пустой список, если файл не существует, не читается,
    или содержимое не является списком.
    """
    if not os.path.isfile(file_path):
        logger.warning(f"Файл не найден: {file_path}")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.debug(f"Успешно загружен список из файла: {file_path}")
                return data
            else:
                logger.warning(f"Файл не содержит список: {file_path}")
                return []
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Ошибка при загрузке JSON-файла: {e}")
        return []


if __name__ == "__main__":
    transactions = load_json_file("../data/operations.json")
    print(transactions)
