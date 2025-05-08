def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """
    Функция принимает на вход список словарей и возвращает отфильтрованный список
    по значению 'state'
    """
    return [i for i in data if i["state"] == state]


def sort_by_date(data: list, reverse: bool = True) -> list:
    """
    Функция принимает на вход список словарей и возвращает отсортированный список
    по значению 'date' по убыванию
    """
    return [time for time in sorted(data, key=lambda x: x["date"], reverse=reverse)]


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
