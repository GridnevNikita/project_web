from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_string: str) -> str:
    """
    Функция, которая принимает на вход данные о карте,
    счете и выводит с маскировкой
    """
    if "Счет" in input_string:
        account_part = input_string.split()
        return f"Счет {get_mask_account(account_part[-1])}"
    else:
        card_part = input_string.split()
        return f"{' '.join(card_part[:-1])} " f"{get_mask_card_number(card_part[-1])}"


def get_date(date_string: str) -> str:
    """
    Функция, которая принимает на вход данные о дате
    и выводит в удобный формат
    """
    date_part = date_string.split("T")[0]
    year, month, day = date_part.split("-")
    result = f"{day}.{month}.{year}"
    return result


if __name__ == "__main__":
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Счет 35383033474447895560"))
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))
