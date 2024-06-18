def filter_by_state(processing_list: list):
    result = []
    for i in processing_list:
        if i['state'] == 'EXECUTED':
            result.append(i)
    return result


def sort_by_date(info: list, asc=True) -> list[str]:
    result = sorted(info, key=lambda x: x['date'], reverse=not asc)
    return result
