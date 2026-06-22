def no_invalid_char(sudoku) -> bool:
    valid_char = [1,2,3,4,5,6,7,8,9," "]
    for row in sudoku:
        for cell in row:
            if cell not in valid_char:
                print(f"'{cell}' is not a valid character in this sudoku grid")
                return False

    return True

def is_row_correct(row: list):
    numbers = [1,2,3,4,5,6,7,8,9]
    for number in numbers:
        occurance_of_number = row.count(number)
        if occurance_of_number > 1:
            return False
    return True

def is_column_correct(sudoku: list, column_index: int):
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

    #print(no_invalid_char(sudoku_correct))
    #print(is_row_correct([1,2," ",4,5,6,7," ",9]))
    print(is_square_correct(sudoku_wrong, 0, 0))



