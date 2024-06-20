from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str = "USD") -> Iterator[dict]:
    """
    Функция фильтрации списка транзакций по виду валюты
    :param transactions: Список транзакций
    :param currency: Вид валюты для фильтрации
    :return: Запись, удовлетворяющая условию
    """
    for i in transactions:
        if i['operationAmount'].get('currency').get('code') == currency:
            yield i


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """
    Функция, возвращающая описание вида операции
    :param transactions: Список транзакций
    :return: Описание операции
    """
    for i in transactions:
        yield i['description']


def card_number_generator(from_num: int, to_num: int) -> Iterator[str]:
    """
    Генератор номеров кредитных карт
    :param from_num: Стартовый номер карты
    :param to_num: Конечный номер карты
    :return: Номер карты в виде xxxx xxxx xxxx xxxx
    """
    for i in range(from_num, to_num + 1):
        card_number = "0" * (18 - len(str(i))) + str(i)
        yield card_number[:4] + ' ' + card_number[5:9] + ' ' + card_number[10:14] + ' ' + card_number[14:18]
