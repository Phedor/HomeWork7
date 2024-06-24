from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(payment: str) -> str | None:
    """ Возвращает описание вида аккаунта и его номер """
    if payment.lower().startswith('счет'):
        name, *number = payment.rsplit(' ', maxsplit=1)
        account_number = ''.join(number)
        if account_number.isnumeric() and len(account_number) == 20:
            return f'{name} {get_mask_account(account_number)}'
    else:
        name, *number = payment.rsplit(' ', maxsplit=4)
        account_number = ''.join(number)
        if account_number.isnumeric() and len(account_number) == 16:
            return f'{name} {get_mask_card_number(account_number)}'
    return None


def format_date(abs_date: str) -> str | None:
    """
    Преобразовывает абсолютную дату со времением в iso-формате
    в дату формата "день.месяц.год".
    Если не удалось преобразовать дату в нужный формат,
    то возвращает None.

    Например:
    get_data('2024-06-17T20:45:10.060143')
    '17.06.2024'
    """
    year = abs_date[:4]
    month = abs_date[5:7]
    day = abs_date[8:10]

    if day.isnumeric() and month.isnumeric() and year.isnumeric():
        return f'{day}.{month}.{year}'
    else:
        return None
