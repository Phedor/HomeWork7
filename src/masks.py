def get_mask_card_number(card_number: str) -> str | None:
    """ Возвращает маску номера карты """
    if len(card_number) != 16:
        return None
    while " " in card_number:
        card_number = card_number.replace(" ", "")
    mask = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return mask


def get_mask_account(account_number: str) -> str | None:
    """ Возвращает маску номера счета
    :type account_number: Номер счета
    """
    if len(account_number) != 20:
        return None
    mask = "**" + account_number[-4:]
    return mask
