def no_invalid_char(sudoku) -> bool:
    valid_char = [1,2,3,4,5,6,7,8,9," "]
    for row in sudoku:
        for cell in row:
            if cell not in valid_char:
                return False

    return True

def is_row_correct(row: list):
    """
    Checks if there are any repeated entries in row, invalidating it.
    """
    numbers = [1,2,3,4,5,6,7,8,9]
    for number in numbers:
        occurance_of_number = row.count(number)
        if occurance_of_number > 1:
            return False
    return True

def is_column_correct(sudoku: list, column_index: int):
    """
    Checks if there are any repeated entries in column, invalidating it. 
    (It is isolated to one column incase I want to create another 
    function which only checks if an entry invalidates a sudoku. 
    In this way I would only be checking one row, one column and one square.)
    """
    column = []
    for row in sudoku:
        column.append(row[column_index])

    return is_row_correct(column)

def is_square_correct(sudoku: list, row_index: int, column_index: int):
    """
    This functions compares the 3 by 3 square of sudoku entries 
    with the index providing the upper most left of that square.
    The indexes that provide the wanted 9 regions are 
    [0,0],[0,3],[0,6]
    [3,0],[3,3],[3,6]
    [6,0],[6,3],[6,6]
    But this function does not restrict to just these value.
    """
    square_list = []
    for i in range(3):
        for j in range(3):
            square_list.append(sudoku[row_index + i][column_index + j])
    
    return is_row_correct(square_list)

def is_sudoku_valid(sudoku: list):
    """
    Calls all check functions to make sure that the sudoku is valid.
    """
    if not no_invalid_char(sudoku):
        return False
    
    for row in sudoku:
        if not is_row_correct(row):
            return False
    
    for column in range(9):
        if not is_column_correct(sudoku, column):
            return False
        
    for i in [0,3,6]:
        for j in [0,3,6]:
            if not is_square_correct(sudoku, i, j):
                return False

    return True



if __name__ == "__main__":
    # sudoku[row][column]
    sudoku_correct = [
        [1,2,3,4,5,6,7,8,9],
        [4," "," "," "," "," "," "," "," "],
        [5," "," "," "," "," "," "," "," "],
        [2," "," "," "," "," "," "," "," "],
        [3," "," "," "," "," "," "," "," "],
        [6," "," "," "," "," "," "," "," "],
        [7," "," "," "," "," "," "," "," "],
        [8," "," "," "," "," "," "," "," "],
        [9," "," "," "," "," "," "," "," "],
    ]

    sudoku_wrong = [
        [1,2,3,4,5,6,7,8,9],
        [4,2," "," "," "," "," "," "," "],
        [5," "," "," ","X"," "," "," "," "],
        [2," "," "," "," "," "," "," "," "],
        [3," "," "," "," "," "," "," "," "],
        [6," "," "," "," "," "," "," "," "],
        [7," "," "," "," "," "," "," "," "],
        [8," "," "," "," "," "," "," "," "],
        [9," "," "," "," "," "," "," "," "],
    ]


