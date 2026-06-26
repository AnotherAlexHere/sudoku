def no_invalid_char(sudoku) -> bool:
    """
    Checks to make sure that the sudoku only contains one of [1,2,3,4,5,6,7,8,9," "].
    """
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

def compare_current_complete(sudoku: list, completed_sudoku: list):
    """
    Returns True is they are comparable (sudoku does not have to be complete), returns False if any of the entries are incorrect.
    """
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != completed_sudoku[i][j] and sudoku[i][j] != " ":
                return False
            
    return True

if __name__ == "__main__":
    # sudoku[row][column]
    # sudoku_correct = [
    #     [1,2,3,4,5,6,7,8,9],
    #     [4," "," "," "," "," "," "," "," "],
    #     [5," "," "," "," "," "," "," "," "],
    #     [2," "," "," "," "," "," "," "," "],
    #     [3," "," "," "," "," "," "," "," "],
    #     [6," "," "," "," "," "," "," "," "],
    #     [7," "," "," "," "," "," "," "," "],
    #     [8," "," "," "," "," "," "," "," "],
    #     [9," "," "," "," "," "," "," "," "],
    # ]

    # sudoku_wrong = [
    #     [1,2,3,4,5,6,7,8,9],
    #     [4,2," "," "," "," "," "," "," "],
    #     [5," "," "," ","X"," "," "," "," "],
    #     [2," "," "," "," "," "," "," "," "],
    #     [3," "," "," "," "," "," "," "," "],
    #     [6," "," "," "," "," "," "," "," "],
    #     [7," "," "," "," "," "," "," "," "],
    #     [8," "," "," "," "," "," "," "," "],
    #     [9," "," "," "," "," "," "," "," "],
    # ]

    sudoku = [
        [" ",3,5,2,6,9,7,8,1],
        [6,8,2,5,7,1,4,9,3],
        [1,9,7,8,3,4,5,6,2],
        [8,2,6,1,9,5,3,4,7],
        [3,7,4,6,8,2,9,1,5],
        [9,5,1,7,4,3,6,2,8],
        [5,1,9,3,2,6,8,7,4],
        [2,4,8,9,5,7,1,3,6],
        [7,6,3,4,1,8,2,5,9]
    ]


    completed_sudoku = [
        [4,3,5,2,6,9,7,8,1],
        [6,8,2,5,7,1,4,9,3],
        [1,9,7,8,3,4,5,6,2],
        [8,2,6,1,9,5,3,4,7],
        [3,7,4,6,8,2,9,1,5],
        [9,5,1,7,4,3,6,2,8],
        [5,1,9,3,2,6,8,7,4],
        [2,4,8,9,5,7,1,3,6],
        [7,6,3,4,1,8,2,5,9]
    ]

    print(compare_current_complete(sudoku,completed_sudoku))
