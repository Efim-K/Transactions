import json
from operator import itemgetter
from zipfile import ZipFile


def load_operation(data_file):
    """
    Загрузка данных из файла из архива и получение актуального списка последних операций
    :param data_file: исходный zip файл с данными
    :return: отсортированный список данных
    """
    # проверяем наличие файла
    if not data_file.exists():
        print('Отсутствует файл данных')
        return []

    # получаем данные из zip файла
    with ZipFile(data_file, 'r') as zip_file:
        name_file = zip_file.namelist()
        with zip_file.open(name_file[0], 'r') as unzip_file:
            operation_list = json.load(unzip_file)

    return operation_list


def get_executed_operations(operations):
    """
    Получаем список операций, выполненных действиями клиента
    :param operations: загруженный список словарей всех действий клиента
    :return: список словарей выполненных действий
    """
    return [
        operation
        for operation in operations
        if operation.get("state") == "EXECUTED"
    ]


def get_sorted_operations_by_date(operations):
    """
    Сортируем операции по дате, начиная с последней
    :param operations:список словарей операций
    :return:отсортированный список словарей по дате
    """
    return sorted(operations, key=itemgetter('date'), reverse=True)


def convert_date(operation_date: str):
    """
    Преобразовывает строку с датой из базы данных операций в строку даты формата ДД.ММ.ГГГГ
    :param operation_date: строка
    :return: f строка
    """
    date = operation_date[:10]
    return f'{date[8:10]}.{date[5:7]}.{date[0:4]}'


def encrypt_payment_info(payment_info: str):
    """
    Преобразовывает информацию платежей операций
    :param payment_info: строка операции платежа
    :return: f строка
    """
    if payment_info.startswith('Счет'):
        return f'Счет **{payment_info[-4:]} '
    elif payment_info != '':
        return (
            f'{payment_info[:-12]}'
            f' {payment_info[-11:-9]}'
            f'** **** {payment_info[-4:]} '
        )
    return ''
