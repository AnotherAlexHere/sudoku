from is_sudoku_valid import *

def test_sudoku_empty():
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

def test_sudoku_improper_char():
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

    #print(is_row_correct([1,2," ",4,5,6,7," ",9]))
    #print(is_square_correct(sudoku_wrong, 0, 0))
    #print(is_sudoku_valid(sudoku_correct))

def test_row_correct():
    assert is_row_correct([1,2," ",4,5,6,7," ",9]) == True, "all numbers only appear once in row, should return True"
    assert is_row_correct([1,2," ",4,5,6,6," ",9]) == False, "number 6 is in the row twice, should return False"
