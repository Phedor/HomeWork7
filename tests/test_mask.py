from src.masks import get_mask_card_number, get_mask_account


def test_masks() -> None:
    assert get_mask_card_number('') is None
    assert get_mask_account('') is None
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'
    assert get_mask_account('73654108430135874305') == '**4305'
