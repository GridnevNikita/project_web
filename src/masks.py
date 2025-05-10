def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает маскированный номер карты
    """
    if not isinstance(card_number, str):
        raise TypeError("Номер карты должен быть строкой")

    if card_number is "":
        raise ValueError("Номер карты не может быть пустым")

    if len(card_number) != 16:
        raise ValueError("Номер карты должен содержать ровно 16 цифр")

    if not card_number.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")

    mask_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return mask_number


def get_mask_account(account_number: str) -> str:
    """
    Функция принимает на вход номер cчёта и возвращает маскированный номер
    """
    if not isinstance(account_number, str):
        raise TypeError("Номер счёта должен быть строкой")

    if account_number is "":
        raise ValueError("Номер счёта не может быть пустым")

    if len(account_number) != 20:
        raise ValueError("Номер счёта должен содержать ровно 20 цифр")

    if not account_number.isdigit():
        raise ValueError("Номер счёта должен содержать только цифры")

    mask_account = f"**{account_number[-4:]}"
    return mask_account


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
