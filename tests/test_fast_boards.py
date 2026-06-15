from sudokusolver.models.sudoku_board import SudokuBoard
from sudokusolver.logic.backtrack import backtrack

# In comments, "dataset" refers to the kaggle.com dataset "4 million Sudoku Puzzles Easy-to-Hard"
# This dataset is by user "RYANAN" at the link https://www.kaggle.com/datasets/informoney/4-million-sudoku-puzzles-easytohard
# (Link is live as of 2026-06-14)

# This dataset is distributed under the CC BY-NC-SA 4.0 License. Details can be found here:
# https://creativecommons.org/licenses/by-nc-sa/4.0/

def run_test(test_array: list[int]) -> tuple[SudokuBoard, SudokuBoard, int]:
    input_board = SudokuBoard()
    input_board.initialize_board(test_array)

    solved_board, result = backtrack(input_board)

    return solved_board, input_board, result

def run_and_assert(test_array: list[int]) -> None:
    solved_board, input_board, result = run_test(test_array)

    assert result == 1
    assert solved_board.is_correct() == 1
    assert solved_board.is_compatible_with(input_board) == 1

def test_easy_1():  # sudoku.com
    test_array =    [0, 0, 4, 0, 5, 0, 0, 0, 0,
                    9, 0, 0, 7, 3, 4, 6, 0, 0,
                    0, 0, 3, 0, 2, 1, 0, 4, 9,
                    0, 3, 5, 0, 9, 0, 4, 8, 0, 
                    0, 9, 0, 0, 0, 0, 0, 3, 0, 
                    0, 7, 6, 0, 1, 0, 9, 2, 0, 
                    3, 1, 0, 9, 7, 0, 2, 0, 0, 
                    0, 0, 9, 1, 8, 2, 0, 0, 3, 
                    0, 0, 0, 0, 6, 0, 1, 0, 0]
        
    run_and_assert(test_array)

def test_easy_2():  # sudoku.com
    test_array =    [0, 0, 1, 0, 0, 2, 4, 0, 6,
                    6, 0, 0, 0, 0, 5, 0, 1, 8,
                    0, 8, 2, 9, 1, 6, 0, 0, 0,
                    0, 0, 0, 8, 0, 4, 5, 0, 0, 
                    1, 0, 8, 0, 0, 0, 6, 0, 9, 
                    0, 0, 0, 0, 0, 0, 8, 2, 7, 
                    5, 1, 4, 7, 3, 0, 0, 6, 2, 
                    3, 0, 7, 2, 4, 0, 0, 0, 0, 
                    0, 2, 0, 0, 0, 1, 3, 7, 0]
    

    run_and_assert(test_array)

def test_medium():  # sudoku.com
    test_array =    [0,0,9,0,6,5,0,2,0,
                    0,6,0,0,0,4,5,8,0,
                    5,0,8,0,2,9,7,0,0,
                    9,0,0,6,0,8,4,7,2,
                    0,0,0,9,1,7,0,0,8,
                    6,0,0,0,0,0,9,0,1,
                    0,4,5,0,0,0,8,0,0,
                    7,0,0,5,8,1,3,0,4,
                    0,0,0,7,0,3,2,0,0]
    
    run_and_assert(test_array)

def test_hard():    # sudoku.com
    test_array =    [6,0,0,5,0,0,4,0,9,
                    0,3,1,0,4,0,0,0,2,
                    0,0,0,0,0,0,0,1,0,
                    0,0,7,0,9,0,0,0,0,
                    0,9,0,2,0,8,0,0,0,
                    2,0,4,0,0,0,6,9,1,
                    0,0,0,1,0,5,0,0,0,
                    4,0,0,0,0,2,8,0,0,
                    9,0,0,0,0,4,0,6,5]
    
    run_and_assert(test_array)

def test_dataset_1():   # dataset, line 2, 80 clues
    test_array = [3, 2, 7, 4, 5, 6, 8, 9, 1,
                    9, 1, 8, 3, 7, 2, 5, 4, 6,
                    4, 6, 5, 9, 8, 1, 7, 3, 2,
                    5, 3, 2, 8, 6, 4, 1, 7, 9,
                    7, 9, 1, 5, 2, 3, 6, 8, 4,
                    8, 4, 6, 7, 1, 9, 2, 5, 3,
                    6, 5, 3, 1, 4, 8, 9, 2, 7,
                    2, 7, 9, 6, 3, 0, 4, 1, 8,
                    1, 8, 4, 2, 9, 7, 3, 6, 5]
    
    run_and_assert(test_array)

def test_dataset_2():   # dataset, line 496683, 73 clues
    test_array = [4, 3, 7, 1, 8, 9, 5, 6, 2,
                    1, 9, 8, 2, 6, 0, 3, 7, 4,
                    2, 5, 6, 4, 7, 3, 9, 8, 1,
                    5, 8, 2, 3, 4, 6, 7, 1, 9,
                    9, 7, 1, 5, 2, 8, 6, 0, 3,
                    3, 6, 4, 9, 1, 7, 8, 2, 5,
                    8, 1, 0, 6, 3, 2, 4, 9, 7,
                    7, 4, 0, 0, 5, 0, 0, 3, 6,
                    6, 2, 3, 7, 9, 4, 0, 5, 8]
    
    run_and_assert(test_array)

def test_dataset_3():   # dataset, line 1005337, 64 clues
    test_array = [9, 4, 2, 3, 0, 6, 1, 0, 5,
                    7, 1, 5, 0, 2, 9, 0, 6, 8,
                    0, 3, 8, 1, 0, 7, 4, 9, 2,
                    2, 9, 1, 6, 4, 8, 7, 5, 3,
                    8, 6, 4, 7, 3, 0, 9, 0, 1,
                    5, 0, 3, 9, 1, 0, 0, 8, 0,
                    1, 2, 7, 8, 0, 4, 5, 0, 6,
                    3, 0, 6, 2, 7, 1, 8, 4, 9,
                    4, 8, 9, 5, 6, 3, 2, 0, 0]
    
    run_and_assert(test_array)

def test_dataset_4():   # dataset, line 1512267, 56 clues
    test_array = [0, 0, 4, 9, 3, 7, 2, 5, 6,
                    0, 3, 9, 6, 2, 0, 8, 1, 4,
                    5, 2, 6, 0, 8, 0, 3, 7, 9,
                    0, 7, 0, 3, 0, 9, 1, 6, 0,
                    0, 0, 2, 8, 7, 4, 5, 0, 3,
                    9, 5, 3, 2, 1, 0, 7, 4, 0,
                    3, 6, 0, 0, 4, 0, 0, 0, 0,
                    0, 4, 1, 7, 9, 0, 0, 3, 5,
                    8, 9, 0, 5, 6, 3, 4, 2, 1]
    
    run_and_assert(test_array)

def test_dataset_5():   # dataset, line 2087349, 47 clues
    test_array = [7, 1, 0, 0, 0, 8, 0, 0, 3,
                    0, 0, 0, 7, 0, 0, 8, 2, 9,
                    2, 0, 8, 6, 3, 0, 5, 7, 0,
                    5, 0, 1, 8, 6, 9, 3, 0, 7,
                    4, 7, 0, 5, 2, 0, 0, 8, 0,
                    0, 6, 9, 0, 7, 3, 1, 0, 0,
                    3, 5, 7, 0, 0, 0, 0, 0, 4,
                    0, 4, 6, 3, 0, 0, 0, 1, 8,
                    0, 8, 2, 9, 4, 6, 7, 0, 5]
    
    run_and_assert(test_array)

def test_dataset_6():   # dataset, line 2500568, 40 clues
    test_array = [6, 0, 0, 1, 0, 0, 0, 0, 0,
                    2, 0, 0, 0, 0, 7, 9, 1, 3,
                    9, 0, 0, 0, 2, 0, 0, 0, 0,
                    4, 0, 8, 0, 0, 1, 0, 0, 5,
                    3, 9, 5, 0, 0, 0, 7, 6, 1,
                    7, 6, 1, 9, 3, 0, 4, 0, 8,
                    1, 7, 9, 0, 0, 0, 8, 0, 0,
                    5, 3, 0, 0, 8, 0, 1, 0, 0,
                    0, 4, 6, 0, 0, 9, 5, 3, 2]
    
    run_and_assert(test_array)

def test_dataset_7():   # dataset, line 3007477, 32 clues
    test_array = [2, 0, 0, 8, 0, 0, 6, 0, 7,
                    0, 9, 7, 0, 0, 0, 0, 0, 5,
                    3, 0, 0, 9, 0, 6, 2, 0, 1,
                    0, 0, 0, 0, 0, 0, 5, 6, 0,
                    0, 0, 8, 6, 9, 5, 0, 2, 0,
                    0, 0, 9, 0, 0, 0, 0, 0, 8,
                    9, 7, 0, 1, 0, 0, 0, 0, 0,
                    0, 0, 6, 0, 0, 0, 4, 0, 3,
                    4, 1, 0, 5, 0, 8, 0, 0, 2]
    
    run_and_assert(test_array)

def test_dataset_8():   # dataset, line 3505890, 24 clues
    test_array = [6, 0, 0, 0, 9, 0, 0, 0, 7,
                    0, 0, 0, 5, 0, 0, 3, 0, 0,
                    3, 1, 0, 0, 0, 0, 0, 0, 5,
                    0, 0, 0, 0, 6, 0, 0, 3, 0,
                    1, 0, 3, 0, 0, 7, 5, 0, 9,
                    5, 9, 0, 0, 0, 0, 7, 0, 0,
                    0, 0, 1, 0, 0, 0, 0, 0, 0,
                    0, 0, 7, 0, 0, 0, 4, 0, 0,
                    9, 0, 5, 0, 0, 0, 0, 7, 0]
    
    run_and_assert(test_array)

def test_dataset_9():   # dataset, line 4000000, 17 clues
    test_array = [0, 0, 9, 0, 0, 0, 0, 0, 0,
                    7, 3, 0, 0, 0, 0, 0, 0, 5,
                    5, 0, 0, 0, 0, 0, 0, 0, 0,
                    6, 0, 0, 0, 0, 8, 0, 0, 0,
                    0, 0, 5, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 5, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 1, 4, 6, 5, 0,
                    0, 5, 0, 7, 2, 0, 0, 8, 0]
    
    run_and_assert(test_array)

