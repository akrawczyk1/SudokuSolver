from sudoku_board.sudokuboard import SudokuBoard

def main():
    test_board = SudokuBoard()

    test_array = [0, 0, 4, 0, 5, 0, 0, 0, 0,
                  9, 0, 0, 7, 3, 4, 6, 0, 0,
                  0, 0, 3, 0, 2, 1, 0, 4, 9,
                  0, 3, 5, 0, 9, 0, 4, 8, 0, 
                  0, 9, 0, 0, 0, 0, 0, 3, 0, 
                  0, 7, 6, 0, 1, 0, 9, 2, 0, 
                  3, 1, 0, 9, 7, 0, 2, 0, 0, 
                  0, 0, 9, 1, 8, 2, 0, 0, 3, 
                  0, 0, 0, 0, 6, 0, 1, 0, 0]

    test_board.initialize_board(test_array)

    test_board.print()

if __name__ == "__main__":
    main()
