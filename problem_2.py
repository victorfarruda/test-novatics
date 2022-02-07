def column(matrix, i):
    return [row[i] for row in matrix]


def validate_items(items):
    items_line = ' '.join(items).replace('.', '').split()
    list_items_list = list(map(lambda x: int(x), items_line))
    list_items_list.sort()

    list_items_set = list(set(list_items_list))
    list_items_set.sort()
    assert list_items_list == list_items_set


def validate_sudoku(board):
    """
        >>> board_true = [
        ... ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ... ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        ... [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ... ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ... ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ... ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        ... [".", "6", ".", ".", ".", ".", "2", "8", "."],
        ... [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        ... [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ... ]
        >>> print(validate_sudoku(board_true))
        output: true
        >>> board_false = [
        ... ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ... ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        ... [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ... ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ... ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ... ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        ... [".", "6", ".", ".", ".", ".", "2", "8", "."],
        ... [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        ... [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ... ]
        >>> print(validate_sudoku(board_false))
        output: false
    """
    try:
        for line in board:
            validate_items(line)

        line_len = len(board[0])
        for i in range(line_len):

            validate_items(column(board, i))

        return 'output: true'
    except Exception as e:
        return 'output: false'


if __name__ == '__main__':
    import doctest

    doctest.testmod()
