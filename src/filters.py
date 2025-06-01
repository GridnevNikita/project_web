import re
from collections import Counter
from typing import List, Dict, Any

def filter_by_description(my_transactions: List[Dict[str, Any]], keyword: str) -> List[Dict[str, Any]]:
    """
    Фильтрует транзакции по наличию ключевого слова.
    Возвращает список операций, в которых описание содержит заданное слово (без учёта регистра).
    """
    return [
        transaction
        for transaction in my_transactions
        if re.search(keyword, transaction.get("description", ""), re.IGNORECASE)
    ]


def count_by_category(my_transactions: List[Dict[str, Any]], my_categories: List[str]) -> Dict[str, int]:
    """
    Считает количество операций по заданным категориям (по полю 'description').
    Возвращает словарь {категория: количество}.
    """
    counter = Counter()

    for transaction in my_transactions:
        description = transaction.get("description", "").lower()
        for category in my_categories:
            if category.lower() in description:
                counter[category] += 1

    category_counts = {category: counter.get(category, 0) for category in my_categories}
    return category_counts
