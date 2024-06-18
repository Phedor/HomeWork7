def filter_by_state(processing_list: list[dict], state: object = 'EXECUTED') -> list[dict]:
    """
    Функция фильтрация одобренных/отмененных транзакций
    :param processing_list: список всех транзакций
    :param state: параметр фильтра
    :return: список отобранных транзакций
    """
    result = []
    for i in processing_list:
        if i['state'] == state:
            result.append(i)
    return result


def sort_by_date(processing_list: list[dict], desc: bool = False) -> list[dict]:
    """
    Функция сортировки списка транзакций по дате проведения
    :return: выдает список отсортированных значений, по параметру сортировки
    :param processing_list: список транзакций
    :param desc: вид сортировки по возрастанию/убыванию
    """
    result = sorted(processing_list, key=lambda x: x['date'], reverse=desc)
    return result
