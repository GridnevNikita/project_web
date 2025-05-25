import logging
import os


logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "masks.log")
file_handler = logging.FileHandler(log_path, encoding="utf-8")

file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает маскированный номер карты
    """
    if not isinstance(card_number, str):
        logger.error(f"Ошибка номер карты должен быть строкой")
        raise TypeError("Номер карты должен быть строкой")

    if card_number == "":
        logger.error(f"Ошибка номер карты не может быть пустым")
        raise ValueError("Номер карты не может быть пустым")

    if len(card_number) != 16:
        logger.error(f"Ошибка номер карты должен содержать ровно 16 цифр")
        raise ValueError("Номер карты должен содержать ровно 16 цифр")

    if not card_number.isdigit():
        logger.error(f"Ошибка номер карты должен содержать только цифры")
        raise ValueError("Номер карты должен содержать только цифры")

    mask_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    logger.debug("Номер карты успешно замаскирован")
    return mask_number


def get_mask_account(account_number: str) -> str:
    """
    Функция принимает на вход номер cчёта и возвращает маскированный номер
    """
    if not isinstance(account_number, str):
        logger.error(f"Ошибка номер счёта счёта должен быть строкой")
        raise TypeError("Номер счёта должен быть строкой")

    if account_number == "":
        logger.error(f"Ошибка номер счёта не может быть пустым")
        raise ValueError("Номер счёта не может быть пустым")

    if len(account_number) != 20:
        logger.error(f"Ошибка номер счёта должен содержать ровно 20 цифр")
        raise ValueError("Номер счёта должен содержать ровно 20 цифр")

    if not account_number.isdigit():
        logger.error(f"Ошибка номер счёта должен содержать только цифры")
        raise ValueError("Номер счёта должен содержать только цифры")

    mask_account = f"**{account_number[-4:]}"
    logger.debug("Номер счёта успешно замаскирован")
    return mask_account


if __name__ == "__main__":
    print(get_mask_card_number("1234567890123456"))
    print(get_mask_account("73654108430135874305"))
