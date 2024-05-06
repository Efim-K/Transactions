from src.utils import load_operation, get_executed_operations, get_sorted_operations_by_date, convert_date, \
    encrypt_payment_info
from settings import FILE_PATH_OPERATIONS, LAST_NUMBER_OPERATION


def main():
    list_operation = load_operation(FILE_PATH_OPERATIONS)
    executed_operations = get_executed_operations(list_operation)
    sorted_operations = get_sorted_operations_by_date(executed_operations)

    index_operation = 0
    for operation in sorted_operations:

        # отслеживаем последние успешные операции
        index_operation += 1
        if index_operation > LAST_NUMBER_OPERATION:
            break

        # выводим на печать подготовленную информацию по последним операциям
        print(convert_date(operation.get('date', '')), ' ',
              operation.get('description', ''), '\n',
              encrypt_payment_info(operation.get('from', '')),
              '-> ',
              encrypt_payment_info(operation.get('to', '')), '\n',
              f"{operation.get('operationAmount', '').get('amount', '')} ",
              f"{operation.get('operationAmount', '').get('currency', '').get('name', '')}\n",
              sep=''
              )


if __name__ == '__main__':
    main()
