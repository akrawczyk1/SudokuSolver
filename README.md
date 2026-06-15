# SudokuSolver

### Author: akrawczyk1 (Andrew Krawczyk)

### Project Link: https://github.com/akrawczyk1/SudokuSolver

## Project Details:

### Overview:

Command-line Sudoku solver using constraint propagation and backtracking search.

### Example:

Here is an example of the project run on a puzzle:

```
Puzzle solved in 0.005818 seconds! Puzzle had input string:
504607000081000003007080450000302000300010690010046037028000040063028915000063870

Here is the initial board:
5   4 | 6   7 |       | 
  8 1 |       |     3 | 
    7 |   8   | 4 5   | 
-----------------------
      | 3   2 |       | 
3     |   1   | 6 9   | 
  1   |   4 6 |   3 7 | 
-----------------------
  2 8 |       |   4   | 
  6 3 |   2 8 | 9 1 5 | 
      |   6 3 | 8 7   | 
-----------------------

Here is the solved board:
5 9 4 | 6 3 7 | 1 2 8 | 
2 8 1 | 5 9 4 | 7 6 3 | 
6 3 7 | 2 8 1 | 4 5 9 | 
-----------------------
9 4 6 | 3 7 2 | 5 8 1 | 
3 7 2 | 8 1 5 | 6 9 4 | 
8 1 5 | 9 4 6 | 2 3 7 | 
-----------------------
1 2 8 | 7 5 9 | 3 4 6 | 
7 6 3 | 4 2 8 | 9 1 5 | 
4 5 9 | 1 6 3 | 8 7 2 | 
-----------------------
```

## Motivation and Observations:

This was a personal project I had wanted to write for some time as an excuse to write a recursive algorithm, to practice staging a project in a file tree in a way that made sense, to explore reading and parsing CSV files using pandas, and to explore writing a non-trivial project in Python. On the sudoku side, I learned about several solving strategies, the MRV heuristic, and had fun putting my Python skills to (sort of) good use!

### Dataset issues:
The dataset I used for testing was a 4 million puzzle set from Kaggle by user "RYANAN" at the link https://www.kaggle.com/datasets/informoney/4-million-sudoku-puzzles-easytohard. The longest test I ran was on every 10000th puzzle: this results in testing against 400 puzzles of increasing difficulty.
Note that this dataset is distributed under the CC BY-NC-SA 4.0 License. Details can be found here:
https://creativecommons.org/licenses/by-nc-sa/4.0/

I originally used string comparison to compare my solver's solutions to the published solutions in the dataset. However, I quickly discovered that the solver's solutions frequently disagreed with the published solutions when the number of clues provided was less than roughly 50. As a result of this, I found that the puzzles provided did, in fact, contain many puzzles with non-unique solutions. This doesn't affect the accuracy of my solver; it still provided valid solutions. However, as a result of this, I removed the string comparison test, and fell back exclusively on my constraint satisfaction check -- double checking that the value of each cell appears exactly once within its own row, column, and box, and also checking that the solved puzzle hasn't overwritten any of the filled boxes in the provided unsolved puzzle. For clarity, I left the code that does the string checking in the tests/test_slow_boards.py file, but it is commented out.

## Usage:

This project is easiest to use with the uv package/project manager. For information and installation instructions, visit this page: https://docs.astral.sh/uv/

To install dependencies with uv, first navigate to the project root in a terminal session, and run the command:
```bash
uv sync
```

Then, you should be all set to run the project in your terminal.

### Syntax:

```bash
sudokusolver
```
Runs the project in demo mode. Solves a medium and hard puzzle pulled from sudoku.com.

```bash
sudokusolver --help
```
Shows syntax information for easier use.

```bash
sudokusolver <puzzle_string>
```
Takes an 81-character string representing a sudoku puzzle and solves it. The string consists of each cell from the puzzle, read left to right, top to bottom in reading order. Any blanks
should be represented with the characters '0' or '.'.

***NOTE***: Very difficult puzzles (less than 25 clues) may take approximately a minute to complete. Expected time for an 18 clue puzzle is approximately 75 seconds.

```bash
sudokusolver -f <file_path> or sudokusolver --file <file_path>
```
Takes a designated filepath to a CSV file and reads the file. The correct CSV file format is specified below. The completed puzzles will be output to stdout, along with how long each puzzle took to complete. Pipe the output to a file if you're running on many puzzles.

```bash
sudokusolver -f or sudokusolver --file
```
Adding the file flag but leaving the file parameter empty will attempt to search your current directory for a .csv file. Please note that the program uses the first CSV file it finds.
Feeding it a CSV file that is not properly formatted or having multiple CSV files in the directory will lead to unspecified behavior.

***NOTE***: Large files (approaching tens of thousands of puzzles) may take several minutes to complete.

### CSV File Format:

The CSV file should contain a header in the first row, and all puzzles should be in the first column, as 81-character strings. Either '0' or '.' may be used to designate blank cells.
Any columns other than the first column are ignored.

## Tests:

This project has a suite of pytest tests. If you want to run the basic (fast) tests, please run:
```bash
uv run pytest
```
in your uv environment. This will run the program against several hard-coded example puzzles as well as make sure the object instantiation behaves properly.

If you would like to run a more exhaustive test, you can run:
```bash
uv run python -m pytest -m slow -s
```
First, you must download a test set. The one that I used for this project is by user "RYANAN" at the link https://www.kaggle.com/datasets/informoney/4-million-sudoku-puzzles-easytohard.
Note that this dataset is distributed under the CC BY-NC-SA 4.0 License. Details can be found here:
https://creativecommons.org/licenses/by-nc-sa/4.0/

Put your CSV file in the directory tests/data. The default behavior is for the test suite to test every 10000th puzzle, and output a line detailing its progress every 10 puzzles solved. If you would like to change these behaviors, go to tests/test_slow_boards.py and change the constants SKIP_VALUE (how many lines to skip between puzzles) and PRINT_LINES (how many puzzles the test should wait to print its progress). For example, in the default setup, SKIP_VALUE = 10000 and PRINT_LINES = 10, the tests will try to solve every 10000th puzzle, and output its progress every 10th solve, which is every 100,000th puzzle.

## License:

This codebase and project are licensed under the CC BY-NC 4.0 (Creative Commons Attribution-NonCommercial) license. For full details on sharing, adapting, and distributing,
visit this page: https://creativecommons.org/licenses/by-nc/4.0/