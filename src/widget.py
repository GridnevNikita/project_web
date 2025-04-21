from masks import get_mask_card_number, get_mask_account


def mask_account_card(input_string: str) -> str:
    """
    Функция, которая принимает на вход данные о карте, счете и выводит с маскировкой
    """
    if "Счет" in input_string:
        parts = input_string.split()
        return f"Счет {get_mask_account(parts[-1])}"
    else:
        parts = input_string.split()
        return f"{' '.join(parts[:-1])} {get_mask_card_number(parts[-1])}"


if __name__ == "__main__":
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Счет 35383033474447895560"))
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(mask_account_card("Счет 73654108430135874305"))
