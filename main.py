import os
from typing import List, Dict, Any

from src.utils import load_json_file
from src.data_loader import csv_transactions, excel_transactions
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from src.filters import filter_by_description
from src.widget import mask_account_card, get_date


def main() -> None:
    """
    Основная функция программы для работы с банковскими транзакциями.

    Позволяет пользователю выбрать источник данных (JSON, CSV или XLSX файл),
    затем загружает транзакции из выбранного файла.

    После загрузки:
    - Предлагает фильтровать транзакции по статусу операции (EXECUTED, CANCELED, PENDING).
    - По желанию сортирует транзакции по дате (по возрастанию или убыванию).
    - Позволяет отфильтровать транзакции по валюте (выбор рублевых).
    - Позволяет отфильтровать транзакции по ключевому слову в описании.

    Затем выводит итоговый список транзакций с форматированной датой,
    описанием, маскированными номерами счетов/карт и суммой с валютой.

    В случае ошибок ввода или пустых данных информирует пользователя и корректно завершает работу.
    """
    # Приветствие и выбор источника
    print("Программа: Привет! Добро пожаловать в программу работы "
          "с банковскими транзакциями.")
    print("Программа: Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ").strip()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    transactions: List[Dict[str, Any]] = []

    if choice == "1":
        print("Программа: Для обработки выбран JSON-файл.")
        file_path = os.path.join(base_dir, "data", "operations.json")
        transactions = load_json_file(file_path)
    elif choice == "2":
        print("Программа: Для обработки выбран CSV-файл.")
        file_path = os.path.join(base_dir, "data", "transactions.csv")
        transactions = csv_transactions(file_path)
    elif choice == "3":
        print("Программа: Для обработки выбран XLSX-файл.")
        file_path = os.path.join(base_dir, "data", "transactions_excel.xlsx")
        transactions = excel_transactions(file_path)
    else:
        print("Программа: Некорректный выбор. Завершение работы.")
        return

    if not transactions:
        print("Программа: Файл пуст или содержит некорректные данные.")
        return

    valid_statuses = {"EXECUTED", "CANCELED", "PENDING"}
    while True:
        print("Программа: Введите статус, по которому необходимо выполнить фильтрацию.")
        print(f"Программа: Доступные для фильтрации статусы: {', '.join(valid_statuses)}")
        status_input = input("Пользователь: ").strip().upper()
        if status_input in valid_statuses:
            print(f'Программа: Операции отфильтрованы по статусу "{status_input}"')
            break
        else:
            print(f'Программа: Статус операции "{status_input}" недоступен.')

    # Фильтрация по статусу
    filtered = filter_by_state(transactions, status_input)

    # Сортировка по дате с валидацией
    while True:
        sort_answer = input("Программа: Отсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower()
        if sort_answer == "да":
            while True:
                order = input(
                    "Программа: Отсортировать по возрастанию или по убыванию?\nПользователь: ").strip().lower()
                if order in ("возрастание", "убывание"):
                    reverse = (order == "убывание")
                    filtered = sort_by_date(filtered, reverse=reverse)
                    break
                else:
                    print("Программа: Некорректный ввод. Введите 'возрастание' или 'убывание'.")
            break
        elif sort_answer == "нет":
            break
        else:
            print("Программа: Пожалуйста, введите 'Да' или 'Нет'.")

    # Фильтрация по валюте с валидацией
    while True:
        rub_answer = input("Программа: Выводить только рублевые транзакции? Да/Нет\nПользователь: ").strip().lower()
        if rub_answer == "да":
            filtered = list(filter_by_currency(filtered, "RUB"))
            break
        elif rub_answer == "нет":
            break
        else:
            print("Программа: Пожалуйста, введите 'Да' или 'Нет'.")

    # Фильтрация по описанию с валидацией
    while True:
        desc_answer = input(
            "Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: "
        ).strip().lower()
        if desc_answer == "да":
            keyword = input("Программа: Введите слово:\nПользователь: ").strip()
            filtered = filter_by_description(filtered, keyword)
            break
        elif desc_answer == "нет":
            break
        else:
            print("Программа: Пожалуйста, введите 'Да' или 'Нет'.")

    print("Программа: Распечатываю итоговый список транзакций...\n")

    if not filtered:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"Программа:\nВсего банковских операций в выборке: {len(filtered)}\n")

    for transaction in filtered:
        raw_date = transaction.get("date", "")
        try:
            formatted_date = get_date(raw_date)
        except Exception:
            formatted_date = raw_date.split("T")[0]

        description = transaction.get("description", "")
        from_acc = transaction.get("from", "")
        to_acc = transaction.get("to", "")

        amount = None
        currency = None
        if operation := transaction.get("operationAmount"):
            amount = operation.get("amount")
            currency = operation.get("currency", {}).get("name")
        else:
            amount = transaction.get("amount")
            currency = transaction.get("currency")

        # Вывод даты и описания
        print(f"{formatted_date} {description}")

        # Вывод маскированных счёта/карты
        try:
            if description.lower() == "открытие вклада":
                print(mask_account_card(to_acc))
            elif from_acc and to_acc:
                print(f"{mask_account_card(from_acc)} -> {mask_account_card(to_acc)}")
            elif to_acc:
                print(mask_account_card(to_acc))
            elif from_acc:
                print(mask_account_card(from_acc))
        except Exception as e:
            print(f"[Ошибка маскировки]: {e}")

        # Вывод суммы и валюты
        if amount and currency:
            print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
