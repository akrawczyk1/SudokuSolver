import os
import pandas as pd
import pytest


from sudokusolver.models.sudoku_board import SudokuBoard
from sudokusolver.logic.backtrack import backtrack


# In comments, "dataset" refers to the kaggle.com dataset "4 million Sudoku Puzzles Easy-to-Hard"
# This dataset is by user "RYANAN" at the link https://www.kaggle.com/datasets/informoney/4-million-sudoku-puzzles-easytohard
# (Link is live as of 2026-06-14)

# This dataset is distributed under the CC BY-NC-SA 4.0 License. Details can be found here:
# https://creativecommons.org/licenses/by-nc-sa/4.0/

@pytest.mark.slow
def test_full_dataset():
    SKIP_VALUE = 10000    # how many lines we skip in the dataset after each test
    PRINT_LINES = 10      # how many lines we want to print after
    DATASET_PATH = os.path.join(os.path.dirname(__file__), "data", "sudoku.csv")

    if not os.path.exists(DATASET_PATH):
        pytest.skip(f"Dataset not found at {DATASET_PATH}")

    index = 0

    for chunk in pd.read_csv(DATASET_PATH, dtype=str, chunksize=10000):

        for _, row in chunk.iloc[::SKIP_VALUE].iterrows():
            input_str = row["quizzes"]
            # solution_str = row["solutions"]
            num_clues = int(row["clue_numbers"])

            input_list = []
            # solution_list = []
            for c in input_str:
                input_list.append(int(c))

            # for c in solution_str:
            #     solution_list.append(int(c))

            # input_board, solution_board = SudokuBoard(), SudokuBoard()
            input_board = SudokuBoard()

            input_board.initialize_board(input_list)
            # solution_board.initialize_board(solution_list)

            output_board, ret_value = backtrack(input_board)

            output_board_list = output_board.get_all_values()
            # solution_board_list = solution_board.get_all_values()

            assert ret_value == 1
            
            
            if output_board.is_correct() == 1:
                pass
            else:
                assert False, f"===ERROR=== Invalid solution for puzzle {index}; input string is: {input_str}, with num clues: {num_clues}"

            assert output_board.is_compatible_with(input_board), f"===ERROR=== Something from the input board {index} got overwritten; input string is: {input_str}, with num clues: {num_clues}"

            if index % (PRINT_LINES * SKIP_VALUE) == 0:
                print(f"Done with line {index}")

            index += SKIP_VALUE
        
        

        
