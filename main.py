from src.processing.homework_functions import filter_by_state, sort_by_date

print('Hello! Let\'s try to make operations')

test_lists = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
              {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
              {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
              {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
              ]

''' First test with 'state' by default '''
print(filter_by_state(test_lists))

''' Second test when 'state' is 'EXECUTED' '''
print(filter_by_state(test_lists, 'EXECUTED'))

''' The third test with other state'''
print(filter_by_state(test_lists, 'CANCELED'))

''' Try to sort lists by default (True) '''
print(sort_by_date(test_lists))

''' Try to sort lists with sort option as True'''
print(sort_by_date(test_lists, True))

''' Try to sort lists with sort option (for example False) '''
print(sort_by_date(test_lists, False))
