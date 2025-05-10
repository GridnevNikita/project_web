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
    return [i for i in data if i.get("state") == state]


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
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
    return sorted(data, key=lambda x: x.get("date"), reverse=reverse)


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
