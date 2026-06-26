from displaying_sudoku import print_sudoku

def ask_for_input():
    """
    Asks user for input, if user provides inputs that are not 
    within the appropriate ranges, it prompts the user to re-enter.
    output = (entry, row, column).
    """
    while True:
        try:
            entry = int(input("Please type in the number you would like to add to the sudoku: "))
            row = int(input("Please enter the row:"))
            column = int(input("Please enter the column:"))
        except:
            retry_or_quite = input("Enter a valid input or if you would like to quit, type quit:")
            if retry_or_quite == "quit":
                return "quit"
            else:
                continue

        if entry in range(1,10) and row in range(9) and column in range(9):
            break
        else:
            print("Make sure your entry is valid,\n" \
            "entry should be a number from 1 to 9,\n" \
            "row and column should be numbers from 0 to 8.")

    return (entry, row, column)

def add_entry(sudoku:list, entry: int, row: int, column: int):
    """
    Enters the number in the desired location of the sudoku as 
    long as that location is empty. Does not discriminate/check 
    whether the addition produces a valid sudoku.

    """
    if sudoku[row][column] == " ":
        sudoku[row][column] = entry

    return sudoku

def remove_entry(sudoku: list, row: int, column: int):
    """
    Replaces whatever entry in the square specified with blank " ".
    """
    sudoku[row][column] = " "
    return sudoku

def is_entry_filled(sudoku: list, row: int, column: int):
    """
    Returns true if there is already a number in the spot, false if there isn't.
    """
    if sudoku[row][column] == " ":
        return False
    elif sudoku[row][column] != " ":
        return True

def replace_entry(sudoku: list, entry: int, row: int, column):
    """
    Enters the number in the desired location of the sudoku. 
    Does not discriminate/check whether the addition produces a valid sudoku.
    """
    sudoku[row][column] = entry
    return sudoku

def sudoku_complete(sudoku):
    """
    Checks if sudoku is complete (all entries are filled). Does NOT check if it is correct.
    """
    for row in sudoku:
        if " " in row:
            return False
        
    return True

def get_filled_in_squares(sudoku: list):
    """
    Outputs a list of coordinates for the filled in entries, this can be used to make sure the user does not try to alter the base grid.
    """
    filled_in_squares = []
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != " ":
                filled_in_squares.append((i,j))
    
    return filled_in_squares
        
if __name__ == "__main__":
    # sudoku = [
    #     [" ",2," "," "," "," "," "," "," "],
    #     [" "," "," "," "," "," "," "," "," "],
    #     [" "," ",9," "," "," "," "," "," "],
    #     [" "," "," "," "," "," "," "," "," "],
    #     [" "," "," "," "," "," ",1," "," "],
    #     [" "," "," "," "," "," "," "," "," "],
    #     [" "," "," ",3," "," "," "," "," "],
    #     [" "," "," "," "," "," "," "," "," "],
    #     [" "," "," "," "," "," "," "," "," "],
    # ]
        
    # print_sudoku(sudoku)
    # add_entry(sudoku,9,2,3)
    # print_sudoku(sudoku)
    # print(ask_for_input())

    # print(get_filled_in_squares(sudoku))
    pass