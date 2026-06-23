from displaying_sudoku import print_sudoku

def add_entry(sudoku:list, entry: int, row: int, column: int):
    """
    Enters the number in the desired location of the sudoku as 
    long as hat location is empty. Does not discriminate/check 
    whether the addition produces a valid sudoku.

    """
    if sudoku[row][column] == " ":
        sudoku[row][column] = entry

    return sudoku


if __name__ == "__main__":
    sudoku = [
        [" "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "],
    ]
        
    print_sudoku(sudoku)
    add_entry(sudoku,9,2,3)
    print_sudoku(sudoku)