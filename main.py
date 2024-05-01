from src.utils import load_operation, get_last_operation
from settings import FILE_PATH_OPERATIONS, LAST_NUMBER_OPERATION


def main():
    list_operation = load_operation(FILE_PATH_OPERATIONS)
    print(get_last_operation(list_operation, LAST_NUMBER_OPERATION))

if __name__ == '__main__':
    main()
