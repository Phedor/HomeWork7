def get_mask_card_number(card_number: str) -> str:
    """ Возвращает маску номера карты """
    while " " in card_number:
        card_number = card_number.replace(" ", "")
    mask = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return mask


def get_mask_account(account_number: str) -> str:
    """ Возвращает маску номера счета """
    mask = "**" + account_number[-4:]
    return mask
