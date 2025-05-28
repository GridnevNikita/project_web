from typing import List,Dict
import pandas as pd
import os

def csv_transactions(file_path: str) -> List[Dict]:
    """ Считывает транзакции из CSV-файла и возвращает список словарей """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Файл не найден: {file_path}")
    try:
        df = pd.read_csv(file_path,sep=";", encoding="utf-8")
        return df.to_dict(orient="records")
    except Exception as e:
        raise ValueError(f"Ошибка при чтении CSV-файла: {e}")

def excel_transactions(file_path: str) -> List[Dict]:
    """ Считывает транзакции из EXCEL-файла и возвращает список словарей """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Файл не найден: {file_path}")

    try:
        df = pd.read_excel(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        raise ValueError(f"Ошибка при чтении Excel-файла: {e}")


if __name__ == '__main__':
    print(csv_transactions("../data/transactions.csv"))
    print(excel_transactions("../data/transactions_excel.xlsx"))