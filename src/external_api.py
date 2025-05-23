import os
from typing import Dict

import requests
from dotenv import load_dotenv

from src.utils import load_json_file

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = "https://api.apilayer.com/exchangerates_data/latest"


def convert_to_rubles(transaction: Dict) -> float:
    """
    Конвертирует сумму транзакции в рубли
    """
    try:
        amount_str = transaction["operationAmount"]["amount"]
        currency_code = transaction["operationAmount"]["currency"]["code"]
        amount = float(amount_str)
    except (KeyError, TypeError, ValueError):
        return 0.0

    if currency_code == "RUB":
        return amount

    if currency_code not in {"USD", "EUR"}:
        return 0.0

    headers = {"apikey": API_KEY}

    params = {"base": currency_code, "symbols": "RUB"}

    try:
        response = requests.get(URL, headers=headers, params=params)
        response.raise_for_status()
        data: dict = response.json()
        rate = float(data["rates"]["RUB"])
        return amount * rate
    except Exception as e:
        print(f"Ошибка API: {e}")
        return 0.0


if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "..", "data", "operations.json")
    transactions = load_json_file(file_path)
    for transaction in transactions:
        rub_amount = convert_to_rubles(transaction)
        print(f"{transaction['description']}: {rub_amount:.2f} руб.")
