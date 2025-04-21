def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает маскированный номер карты
    """
    mask_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return mask_number


def get_mask_account(account_number: str) -> str:
    """
    Функция принимает на вход номер cчёта и возвращает маскированный номер
    """
    mask_account = f"**{account_number[-4:]}"
    return mask_account


if __name__ == "__main__":
    while True:
        user_card_number = input("Введите ваш номер карты (для выхода введите 'exit'): ")

        if user_card_number.lower() == "exit":
            break

        if len(user_card_number) == 16:
            print(get_mask_card_number(user_card_number))
            break
        else:
            print("\nОшибка: Номер карты должен содержать ровно 16 цифр\n")

    while True:
        user_account = input("Введите ваш номер счёта (для выхода введите 'exit'): ")

        if user_account.lower() == "exit":
            break

        if len(user_account) == 20:
            print(get_mask_account(user_account))
            break
        else:
            print("\nОшибка: Номер счёта должен содержать ровно 20 цифр\n")
