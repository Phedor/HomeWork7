from src.widget import mask_account_card
from src.widget import format_date


def main() -> None:
    print("Тестирование маскировки и отработки ошибок по номеру счетов и карт")
    print(f'Visa Platinum 7000 7922 8960 6361 -'
          f'{(mask_account_card("Visa Platinum 7000 7922 8960 6361") == "Visa Platinum 7000 79** **** 6361")}')
    print(f'Maestro 7000 7922 8960 6361 - '
          f'{(mask_account_card("Maestro 7000 7922 8960 6361") == "Maestro 7000 79** **** 6361")}')
    print(f'Счет 73654108430135874305 - '
          f'{(mask_account_card("Счет 73654108430135874305") == "Счет **4305")}')
    print(f'Visa Electron 7000 - '
          f'{(mask_account_card("Visa Electron 7000") == None)}')
    print(f'zzZzz - '
          f'{(mask_account_card("zzZzz") == None)}')

    print("\nПроверка преобразования дат")
    print(f'"2018-07-11T02:26:18.671407" - '
          f'{(format_date("2018-07-11T02:26:18.671407") == "11.07.2018")}')
    print(f'"2018-AA-11T02:26:18.671407" - '
          f'{(format_date("2018-AA-11T02:26:18.671407"))}')

if __name__ == "__main__":
    main()
