from typing import Callable

from Core.Types import Request


def clean_array(array: list) -> list:
    """Очищает массив от пустых элементов

    Args:
        array (list): Массив элементов

    Returns:
        list: Очищенный массив
    """
    return [i for i in array if i != ""]


def has_request(func: Callable) -> bool:
    args: list = func.__annotations__.items()

    count: int = 0
    for _, arg_type in args:
        if arg_type is Request:
            count += 1

    return True if count == 1 else False
