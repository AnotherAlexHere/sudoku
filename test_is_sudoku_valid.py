from is_sudoku_valid import *

def test_no_invalid_char():
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
    assert is_sudoku_valid(sudoku_wrong) == False

def test_is_row_correct():
    assert is_row_correct([1,2," ",4,5,6,7," ",9]) == True, "all numbers only appear once in row, should return True"
    assert is_row_correct([1,2," ",4,5,6,6," ",9]) == False, "number 6 is in the row twice, should return False"

def test_is_column_correct():
    sudoku_wrong = [
        [1,2,3,4,5,6,7,8,9],
        [4," "," "," "," "," "," "," "," "],
        [5," "," "," "," "," "," "," "," "],
        [2," "," "," "," "," "," "," "," "],
        [3," "," "," "," "," "," "," "," "],
        [6," "," "," "," "," "," "," "," "],
        [7," "," "," "," "," "," "," "," "],
        [9," "," "," "," "," "," "," "," "],
        [9," "," "," "," "," "," "," "," "],
    ]

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
    
    assert is_column_correct(sudoku_wrong, 0) == False, "There are two 9s in that column so should return False."
    assert is_column_correct(sudoku_correct, 0) == True, "Column is valid so should return True."

def test_is_square_correct():
    sudoku_correct = [
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

    sudoku_wrong = [
        [" ",3,5,2,6,9,7,8,1],
        [6,8,2,5,7,1,4,9,3],
        [1,9,7,8,3,4,5,6,2],
        [8,2,6,1,9,5,3,4,7],
        [3,7,4,6,2,2,9,1,5],
        [9,5,1,7,4,3,6,2,8],
        [5,1,9,3,2,6,8,7,4],
        [2,4,8,9,5,7,1,3,6],
        [7,6,3,4,1,8,2,5,9]
    ]

    assert is_square_correct(sudoku_wrong, 3, 3) == False, "There are two 2s in that square so should return False."
    assert is_square_correct(sudoku_correct, 3, 3) == True, "Square is valid so should return True."

def test_is_sudoku_valid():
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
    assert is_sudoku_valid(sudoku) == True

def test_compare_currect_complete():
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

    assert compare_current_complete(sudoku,completed_sudoku) == True, "While the sudokus are not the same, all the entries that are there match so should return True."

