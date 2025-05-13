from datetime import datetime
from typing import Dict, List


def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует список словарей по определенному состоянию транзакции.

    Параметры:
    data (list[dict]): список словарей с данными транзакций
    state (str): значение состояния для фильтрации.
    По умолчанию 'EXECUTED'.

    Возвращает:
    list[dict]: новый список словарей, содержащих только транзакции
    с указанным состоянием.
    """
    # Добавляем проверку типа данных
    if not isinstance(data, list):
        raise TypeError("data должен быть списком словарей")

    # Добавляем проверку наличия ключа state
    filtered = []
    for item in data:
        if not isinstance(item, dict):
            raise TypeError("Элементы data должны быть словарями")
        if "state" not in item:
            raise ValueError("В каждом словаре должен быть ключ 'state'")
        if item["state"] == state:
            filtered.append(item)

    return filtered


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по дате в формате ISO.

    Параметры:
    data (list[dict]): список словарей с данными транзакций
    reverse (bool, optional): флаг сортировки.
    True - сортировка по убыванию (по умолчанию),
    False - сортировка по возрастанию.

    Возвращает:
    list[dict]: отсортированный список словарей.
    """
    # Добавляем проверку типа данных
    if not isinstance(data, list):
        raise TypeError("data должен быть списком словарей")

    # Добавляем проверку наличия ключа date
    for item in data:
        if not isinstance(item, dict):
            raise TypeError("Элементы data должны быть словарями")
        if "date" not in item:
            raise ValueError("В каждом словаре должен быть ключ 'date'")

    return sorted(
        data,
        key=lambda x: datetime.strptime(x.get("date", "0001-01-01T00:00:00"), "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=reverse,
    )


if __name__ == "__main__":
    filtered_data = filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )

    for item in filtered_data:
        print(item)

    sorted_data = sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )

    for item in sorted_data:
        print(item)
