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


def get_last_operation(operation_list, last_operation):
    """
    Создает строку с последними операциями, выполненных клиентом
    :param operations: список операций клиента
    :param last_operation: количество последних операций для вывода
    :return: строка с последними операциями
    """
    # создаем список словарей на соответствие структуры данных
    operation_list_new = [i for i in operation_list if 'date' in i]

    # сортируем список по дате
    operations = sorted(operation_list_new, key=itemgetter('date'), reverse=True)

    operation_last_view = ''
    index_operation = 0
    # получаем список последних выполненных операций и преобразовываем для вывода
    for i in range(len(operations)):
        if operations[i]['state'] != 'EXECUTED':
            continue

        # отслеживаем последние успешные операции
        index_operation += 1
        if index_operation > last_operation:
            break

        # добавляем в вывод дату операции
        date = operations[i]['date'][:10]
        operation_last_view += f'{date[8:10]}.{date[5:7]}.{date[0:4]}'
        # добавляем в вывод наименование операции
        operation_last_view += f' {operations[i]['description']}\n'

        # добавляем в вывод откуда пришел перевод
        if "from" in operations[i]:
            if operations[i]['from'][:4] == 'Счет':
                operation_last_view += f'Счет **{operations[i]["from"][-4:]} '
            else:
                operation_last_view += (f'{operations[i]["from"][:-12]}'
                                        f' {operations[i]["from"][-11:-9]}'
                                        f'** **** {operations[i]["from"][-4:]} '
                                        )

        # добавляем в вывод куда пришел перевод
        if "to" in operations[i]:
            if operations[i]["to"][:4] == 'Счет':
                operation_last_view += f'-> Счет **{operations[i]["to"][-4:]}\n'
            else:
                operation_last_view += (f'-> {operations[i]["to"][:-12]}'
                                        f' {operations[i]["to"][-11:-9]}'
                                        f'** **** {operations[i]["to"][-4:]}\n'
                                        )

        # добавляем в вывод сумму операции
        operation_last_view += (f'{operations[i]["operationAmount"]["amount"]} '
                                f'{operations[i]["operationAmount"]["currency"]["name"]}\n\n'
                                )

    return operation_last_view
