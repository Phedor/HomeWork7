import pytest
from src.widget import mask_account_card, format_date


def test_widget_date_convert() -> None:
    assert format_date('2018-07-11T02:26:18.671407') == '11.07.2018'
    assert format_date('20AAAAA-11T02:26:18.671407') is None


@pytest.mark.parametrize('account, result',
                         [
                             ('Visa Platinum 7000 7922 8960 6361', 'Visa Platinum 7000 79** **** 6361'),
                             ('Visa Platinum 7000', None),
                             ('Счет 73654108430135874305', 'Счет **4305'),
                             ('Счет 7365', None)
                         ])
def test_widget_mask(account: str, result: str | None) -> None:
    """
    Тестирование маски номеров карт и счетов
    :param account_list: Список номеров и счетов
    :param result: Ожидаемый результат
    :return: None
    """
    assert mask_account_card(account) == result
