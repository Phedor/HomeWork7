from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, format_date

def test_masks():
    assert get_mask_card_number('') == None
    assert get_mask_account('') == None
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'
    assert get_mask_account('73654108430135874305') == '**4305'

def test_widget():
    assert mask_account_card('Visa Platinum 7000 7922 8960 6361') == 'Visa Platinum 7000 79** **** 6361'
    assert mask_account_card('Visa Platinum 7000') == None
    assert mask_account_card('Счет 73654108430135874305') == 'Счет **4305'
    assert mask_account_card('Счет 7365') == None

    assert format_date('2018-07-11T02:26:18.671407') == '11.07.2018'
    assert format_date('20AAAAA-11T02:26:18.671407') == None
