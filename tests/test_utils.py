import pathlib

from src.utils import get_last_operation, load_operation

test_file = pathlib.Path('xx')


def test_load_operation():
    assert load_operation(test_file) == []


json_dict_ask = [
    {
        "id": 41428829,
        "state": "xxx",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    },
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "to": "Счет 35383033474447895560"
    },
    {
        "id": 41428824,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    },
]
json_dict_ask_2 = [
    {
        "id": 41428824,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    },
]
json_dict_ask_3 = [
    {
        "id": 41428824,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
            }
        },
        "description": "Перевод организации",
        "from": "Счет 1596837868705199",
        "to": "Maestro 64686473678894779589"
    },
]

answer = ('26.08.2019 Перевод организации\n'
          'Maestro 1596 37** **** 5199 -> Счет **9589\n'
          '31957.58 руб.\n\n')
answer_2 = ('26.08.2019 Перевод организации\n'
            'Maestro 1596 37** **** 5199 -> Счет **9589\n'
            '31957.58 руб.\n\n'
            '30.06.2018 Перевод организации\n'
            '-> Счет **5560\n'
            '9824.07 USD\n\n')
answer_3 = ('26.08.2019 Перевод организации\n'
          'Счет 1596 37** **** 5199 -> Maestro **9589\n'
          '31957.58 руб.\n\n')

def test_get_last_operation():
    assert get_last_operation(json_dict_ask, 1) == answer
    assert get_last_operation(json_dict_ask_2, len(json_dict_ask_2) + 2) == answer
    assert get_last_operation([], 1) == ''
    assert get_last_operation(json_dict_ask, 0) == ''
    assert get_last_operation(json_dict_ask, 2) == answer_2
    assert get_last_operation(json_dict_ask_3, 2) == answer_3
