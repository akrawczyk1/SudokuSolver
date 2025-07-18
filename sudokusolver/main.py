from sudoku_board.sudokuboard import SudokuBoard
from sudoku_logic.simplelogic import run_simple_logic
from sudoku_logic.simplelogic import check_board

def main(): 
    test_board = SudokuBoard()

    # Easy Board
    # test_array = [0, 0, 4, 0, 5, 0, 0, 0, 0,
    #               9, 0, 0, 7, 3, 4, 6, 0, 0,
    #               0, 0, 3, 0, 2, 1, 0, 4, 9,
    #               0, 3, 5, 0, 9, 0, 4, 8, 0, 
    #               0, 9, 0, 0, 0, 0, 0, 3, 0, 
    #               0, 7, 6, 0, 1, 0, 9, 2, 0, 
    #               3, 1, 0, 9, 7, 0, 2, 0, 0, 
    #               0, 0, 9, 1, 8, 2, 0, 0, 3, 
    #               0, 0, 0, 0, 6, 0, 1, 0, 0]
    
    # Easy board Sudoku.com
    # test_array = [0, 0, 1, 0, 0, 2, 4, 0, 6,
    #               6, 0, 0, 0, 0, 5, 0, 1, 8,
    #               0, 8, 2, 9, 1, 6, 0, 0, 0,
    #               0, 0, 0, 8, 0, 4, 5, 0, 0, 
    #               1, 0, 8, 0, 0, 0, 6, 0, 9, 
    #               0, 0, 0, 0, 0, 0, 8, 2, 7, 
    #               5, 1, 4, 7, 3, 0, 0, 6, 2, 
    #               3, 0, 7, 2, 4, 0, 0, 0, 0, 
    #               0, 2, 0, 0, 0, 1, 3, 7, 0]

    # Medium board Sudoku.com
    test_array = [0,0,9,0,6,5,0,2,0,
                  0,6,0,0,0,4,5,8,0,
                  5,0,8,0,2,9,7,0,0,
                  9,0,0,6,0,8,4,7,2,
                  0,0,0,9,1,7,0,0,8,
                  6,0,0,0,0,0,9,0,1,
                  0,4,5,0,0,0,8,0,0,
                  7,0,0,5,8,1,3,0,4,
                  0,0,0,7,0,3,2,0,0]
    
    # Hard board Sudoku.com #TODO Not able to solve
    # test_array = [6,0,0,5,0,0,4,0,9,
    #               0,3,1,0,4,0,0,0,2,
    #               0,0,0,0,0,0,0,1,0,
    #               0,0,7,0,9,0,0,0,0,
    #               0,9,0,2,0,8,0,0,0,
    #               2,0,4,0,0,0,6,9,1,
    #               0,0,0,1,0,5,0,0,0,
    #               4,0,0,0,0,2,8,0,0,
    #               9,0,0,0,0,4,0,6,5]
    
    test_board.initialize_board(test_array)
    
    print("Here is the initial board:")
    test_board.print()
    
    result = run_simple_logic(test_board)
    
    if result == 0:
        print("Failed to fill board! Here is the final result:")
    else:
        print("Successfully filled board! Here is the final result:")

    test_board.print()
    
    if check_board(test_board):
        print("Board passes tests! It seems correct!")
    else:
        print("There is an error in the board somewhere!")

if __name__ == "__main__":
    main()
