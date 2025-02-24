from datetime import datetime


def filter_by_state(passed_lists: list[dict], state: str = 'EXECUTED') -> list[dict]:
    '''Функция принимает на вход список словарей с данными о банковских операциях и параметр
    state , возвращает новый список, содержащий только те словари, у которых ключ state
    содержит переданное в функцию значение'''
    result = []
    for tmp_list in passed_lists:
        if 'state' in tmp_list and tmp_list['state'] == state:
            result.append(tmp_list)
    return result


def sort_by_date(passed_lists: list[dict], sort_by_date_forward: bool = True) -> list[dict]:
    '''Функция принимает на вход список словарей и параметр порядка сортировки,
    возвращает новый список, в котором исходные словари отсортированы по дате.
    Порядок направления сортировки по умолчанию True'''

    '''Промежуточная функция возвращающая дату. Без обработки исключений.
    Считаем, что все даты - корректны.'''
    def get_sort_key(passed_list: dict) -> datetime:
        tmp_date_str = passed_list['date']
        return datetime.strptime(tmp_date_str, '%Y-%m-%dT%H:%M:%S.%f')

    return sorted(passed_lists, key=get_sort_key, reverse=not sort_by_date_forward)
