from displaying_sudoku import *
from fill_in_sudoku import *
from is_sudoku_valid import *

def level_one_sudoku_game():
    """
    Plays sudoku game in terminal. Does not check for correctness, or validity. Game is complete when all squares have been filled.
    """

    # sudoku = [
    #     [" "," "," ",2,6," ",7," ",1],
    #     [6,8," "," ",7," "," ",9," "],
    #     [1,9," "," "," ",4,5," "," "],
    #     [8,2," ",1," "," "," ",4," "],
    #     [" "," ",4,6," ",2,9," "," "],
    #     [" ",5," "," "," ",3," ",2,8],
    #     [" "," ",9,3," "," "," ",7,4],
    #     [" ",4," "," ",5," "," ",3,6],
    #     [7," ",3," ",1,8," "," "," "]
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

    originally_filled_squares = get_filled_in_squares(sudoku)

    while True:
        print_sudoku(sudoku)
        user_input = ask_for_input()
        if user_input == "quit":
            print("You chose to quit.")
            break

        if (user_input[1],user_input[2]) in originally_filled_squares:
            print("This square was part of the original sudoku and cannot be changed. Try again.")
            continue

        if is_entry_filled(sudoku, user_input[1], user_input[2]):
            decision = input("You have entered a square that already has an entry, if you would like to replace the entry in that square, type yes.")
            if decision == "yes":
                replace_entry(sudoku, user_input[0], user_input[1], user_input[2])
        elif not is_entry_filled(sudoku, user_input[1], user_input[2]):
            add_entry(sudoku, user_input[0], user_input[1], user_input[2])

        if sudoku_complete(sudoku):
            print_sudoku(sudoku)
            print("Congrats! You have completed the sudoku!")
            break

level_one_sudoku_game()