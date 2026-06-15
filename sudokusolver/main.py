import argparse
import os
from pathlib import Path
import time 

from .models.sudoku_board import SudokuBoard
from .logic.backtrack import backtrack

def handle_board(input_string: str, print_check: bool = True) -> tuple[SudokuBoard, SudokuBoard, int, float]:
    """
    Takes a valid input string of a sudoku board and tries to solve it.
    Returns [input_board, output_board, return_value, solve_time]
    """

    input_board = SudokuBoard()
    board_list = [0 if c == '.' else int(c) for c in input_string]
    input_board.initialize_board(board_list)

    start_time = time.perf_counter()

    output_board, return_code = backtrack(input_board)

    end_time = time.perf_counter()

    if print_check:
        if return_code == 1:
            print(f"Puzzle solved in {end_time - start_time:.6f} seconds! Puzzle had input string:\n{input_string}\n")
            print(f"Here is the initial board:")
            input_board.print()
            print()
            print(f"Here is the solved board:")
            output_board.print()
            print()

        else:
            print("Something went wrong! The puzzle has no valid solution!")
            input_board.print()            

    return input_board, output_board, return_code, end_time - start_time    

def main(): 

    parser = argparse.ArgumentParser(
        prog='sudokusolver',
        description='Solve Sudoku puzzles from the command line.',
    )

    parser.add_argument('puzzle', nargs='?', default=None, 
                        help='An 81-character puzzle string written from left to right, top to bottom, in reading order (digits 1-9, with either 0 or . as blank squares.)'
                        )
    
    parser.add_argument('-f', '--file', nargs='?', const='__search__', default=None, metavar='FILEPATH',  
                        help='Parses a CSV file of puzzles. First column should have a header, and then any number of 81 character strings. Omit a path to search the current directory. '
                            '(Note that multiple CSV files in the current directory will lead to unspecified behavior. Please only run -f on directories with one CSV file.)'
                        )
    
    
    
    args = parser.parse_args()

    if args.file is not None: # CSV Mode
        import pandas as pd
        file_path = args.file
        if file_path == '__search__':
            file_path = next(Path.cwd().glob("*.csv"), None)

        if file_path is None:
            parser.error("There was no .csv found in the current directory!")
        
       
        index = 0
        
        if not os.path.exists(file_path):
            parser.error(f"The file at path {file_path} does not exist!")      

        print(f"Parsing file {file_path}:\n")

        for chunk in pd.read_csv(file_path, dtype=str, chunksize=10000):

            for _, row in chunk.iterrows():
                print(f" ==== TEST {index + 1} ====")
                input_str = row.iloc[0]
                handle_board(input_str)
                index += 1

        

    elif args.puzzle is not None: # String mode
        board_string = args.puzzle.strip()
        
        if len(board_string) != 81:
            parser.error(f"The pasted string had {len(board_string)} character(s)! The length must be 81!")
        
        elif not all(c.isdigit() or c == '.' for c in board_string):
            parser.error(f"The pasted string contains illegal characters! Please make sure the string only contains '0-9' or '.'!")
        
        else:
            handle_board(board_string)

            

    else: # Demo mode
        test_arrays = []
    
        # Medium board Sudoku.com
        test_arrays.append(
            [0,0,9,0,6,5,0,2,0,
            0,6,0,0,0,4,5,8,0,
            5,0,8,0,2,9,7,0,0,
            9,0,0,6,0,8,4,7,2,
            0,0,0,9,1,7,0,0,8,
            6,0,0,0,0,0,9,0,1,
            0,4,5,0,0,0,8,0,0,
            7,0,0,5,8,1,3,0,4,
            0,0,0,7,0,3,2,0,0]
        )

        # Hard board Sudoku.com
        test_arrays.append(
            [6,0,0,5,0,0,4,0,9,
            0,3,1,0,4,0,0,0,2,
            0,0,0,0,0,0,0,1,0,
            0,0,7,0,9,0,0,0,0,
            0,9,0,2,0,8,0,0,0,
            2,0,4,0,0,0,6,9,1,
            0,0,0,1,0,5,0,0,0,
            4,0,0,0,0,2,8,0,0,
            9,0,0,0,0,4,0,6,5]
        )

        for index, array in enumerate(test_arrays):

            test_board = SudokuBoard()
            test_board.initialize_board(array)
        
            print(f"=========== TEST {index + 1} ===========\n")
            print("Here is the initial board:")
            test_board.print()
            
            result_board, return_code = backtrack(test_board)
            
            if return_code == 0:
                print("Failed to fill board! Here is the final result:")
            else:
                print("Successfully filled board! Here is the final result:")

            result_board.print()
            
            if result_board.is_correct() == 1:
                print("Board passes tests! It seems correct!")
            else:
                print("There is an error in the board somewhere!")

            print(f"========= END TEST {index + 1} =========\n")

        print(f"This is the demo mode of the program; it has solved two test puzzles above from sudoku.com.\n"
              f"If you would like to run this program on your own puzzle or a csv file containing puzzles,\n"
              f"please use the --help command to see the correct usage patterns.\n")

if __name__ == "__main__":
    main()
