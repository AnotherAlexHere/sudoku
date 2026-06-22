def print_sudoku(sudoku: list):
    """
    Prints out the sudoku in terminal in somewhat of a readable format (for now)
    """
    print("-------------------------------------------------------")
    for row in sudoku:
        print("|", end="")
        for cell in row:
            print(f"  {cell}  |", end="")
        print("\n-------------------------------------------------------")



if __name__ == "__main__":
    # sudoku[row][column]
    sudoku = [
        [1,2,3,4,5,6,7,8,9],
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


