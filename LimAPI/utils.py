def clean_array(array: list) -> list:
    """Очищает массив от пустых элементов

    Args:
        array (list): Массив элементов

    Returns:
        list: Очищенный массив
    """
    return [i for i in array if i != ""]
