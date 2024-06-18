def filter_by_state(processing_list: list):
    """
    Функция фильтрация одобренных транзакций
    :param processing_list: список всех транзакций
    :return: список отобранных транзакций
    """
    result = []
    for i in processing_list:
        if i['state'] == 'EXECUTED':
            result.append(i)
    return result


def sort_by_date(info: list, asc=True) -> list[str]:
    """
    Функция сортировки списка транзакций по дате проведения
    :param info: список транзакций
    :param asc: вид сортировки возрастание/убывание
    :return: отсортированнй список
    """
    result = sorted(info, key=lambda x: x['date'], reverse=not asc)
    return result
