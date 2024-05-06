import pathlib

from src.utils import load_operation, get_executed_operations, get_sorted_operations_by_date, convert_date, \
    encrypt_payment_info


def test_load_operation():
    assert load_operation(pathlib.Path('xx')) == []


def test_get_executed_operations():
    assert get_executed_operations([{'state': 'EXECUTED'}, {}, {'state': 'E'}]) == [{'state': 'EXECUTED'}]


def test_get_sorted_operations_by_date():
    assert get_sorted_operations_by_date([{'date': 1}, {'date': 3}]) == [{'date': 3}, {'date': 1}]


def test_convert_date():
    assert convert_date('2019-08-26T10:50:58.294041') == '26.08.2019'
    assert convert_date('') == '..'


def test_encrypt_payment_info():
    assert encrypt_payment_info('Счет 35383033474447895560') == 'Счет **5560 '
    assert encrypt_payment_info('MasterCard 7158300734726758') == 'MasterCard 7158 00** **** 6758 '
    assert encrypt_payment_info('') == ''
