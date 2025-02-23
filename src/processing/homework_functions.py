from datetime import datetime

def filter_by_state(passed_lists: list, state:str = 'EXECUTED') -> list:
    '''Функция принимает на вход список словарей с данными о банковских операциях и параметр
    state , возвращает новый список, содержащий только те словари, у которых ключ state
    содержит переданное в функцию значение'''
    result = []
    for tmp_list in passed_lists:
        if state in tmp_list and tmp_list['state'] == state:
            result.append(tmp_list)
    return result


def sort_by_date(passed_lists: list, sort_by_date_forward:bool = 'True') -> list:
    '''Функция принимает на вход список словарей и параметр порядка сортировки,
    возвращает новый список, в котором исходные словари отсортированы по дате.
    Порядок направления сортировки по умолчанию True'''
    result = []
    tmp_date:datetime = datetime.now()
    list_index =
