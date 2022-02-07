def order_list_and_remove_duplicate(input_data: list):
    """
        >>> input_data = [8, 5, 10, 5, 2, 4, 4, 3]
        >>> output_data = order_list_and_remove_duplicate(input_data)
        >>> assert output_data == [2, 3, 4, 5, 8, 10]
    """
    list_without_duplicated_items = list(set(input_data))
    list_without_duplicated_items.sort()
    return list_without_duplicated_items


if __name__ == "__main__":
    import doctest

    doctest.testmod()
