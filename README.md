# SudokuSolver

### Author: akrawczyk1 (Andrew Krawczyk)

### Project Link: https://github.com/akrawczyk1/SudokuSolver

## Project Details:

### Overview:

This is a sudoku solver project. It attempts to use simple sudoku strategies to solve a puzzle like finding naked singles. If that approach fails, it uses recursive backtracking and 
the minimum remaining values (MRV) heuristic to solve more difficult puzzles.

## Usage:

This project is easiest to use with the uv package/project manager. For information and installation instructions, visit this page: https://docs.astral.sh/uv/

To install dependencies with uv, first navigate to the project root in a terminal session, and run the command:
    uv sync

Then, you should be all set to run the project in your terminal.

### Syntax:

    sudokusolver

Runs the project in demo mode. Solves a medium and hard puzzle pulled from sudoku.com.

    sudokusolver --help

Shows syntax information for easier use.

    sudokusolver <puzzle_string>

Takes an 81-character string representing a sudoku puzzle and solves it. The string consists of each cell from the puzzle, read left to right, top to bottom in reading order. Any blanks
should be represented with the characters '0' or '.'.

***NOTE***: Very difficult puzzles (less than 25 clues) may take approximately a minute to complete. Expected time for an 18 clue puzzle is approximately 75 seconds.

    sudokusolver -f <file_path> or sudokusolver --file <file_path>

Takes a designated filepath to a CSV file and reads the file. The correct CSV file format is specified below. The completed puzzles will be output to stdout, along with how long each puzzle took to complete. Pipe the output to a file if you're running on many puzzles.

    sudokusolver -f or sudokusolver --file

Adding the file flag but leaving the file parameter empty will attempt to search your current directory for a .csv file. Please note that the program uses the first CSV file it finds.
Feeding it a CSV file that is not properly formatted or having multiple CSV files in the directory will lead to unspecified behavior.

***NOTE***: Large files (approaching tens of thousands of puzzles) may take several minutes to complete.

### CSV File Format:

The CSV file should contain a header in the first row, and all puzzles should be in the first column, as 81-character strings. Either '0' or '.' may be used to designate blank cells.
Any columns other than the first column are ignored.

## Tests:

This project has a suite of pytest tests. If you want to run the basic (fast) tests, please run:
    uv run pytest
in your uv environment. This will run the program against several hard-coded example puzzles as well as make sure the object instantiation behaves properly.

If you would like to run a more exhaustive test, you can run:
    uv run python -m pytest -m slow -s

First, you must download a test set. The one that I used for this project is by user "RYANAN" at the link https://www.kaggle.com/datasets/informoney/4-million-sudoku-puzzles-easytohard.
Note that his dataset is distributed under the CC BY-NC-SA 4.0 License. Details can be found here:
https://creativecommons.org/licenses/by-nc-sa/4.0/

Put your CSV file in the directory tests/data. The default behavior is for the test suite to test every 10000th puzzle, and output a line detailing its progress every 10 puzzles solved. If you would like to change these behaviors, go to tests/test_slow_boards.py and change the constants SKIP_VALUE (how many lines to skip between puzzles) and PRINT_LINES (how many puzzles the test should wait to print its progress). For example, in the default setup, SKIP_VALUE = 10000 and PRINT_LINES = 10, the tests will try to solve every 10000th puzzle, and output its progress every 10th solve, which is every 100,000th puzzle.

## Comments:

This was a personal project I had wanted to write for some time as an excuse to write a recursive algorithm, to practice staging a project in a file tree in a way that made sense, to explore reading and parsing CSV files using pandas, and to explore writing a non-trivial project in Python. On the sudoku side, I learned about several solving strategies, the MRV heuristic, and had fun putting my Python skills to (sort of) good use!

### Dataset:
The dataset I used above gave me quite a scare at first in testing; I originally had a functionality to intake a published solution string, and compare my solution to the published solution.
To my surprise, once the test suite got to tests with fewer than 50 hints, I started getting several messages saying that my solution was valid, but it differed from the published solution.
However, after further testing, I found that the dataset I used had puzzles with non-unique solutions. It appears that several large datasets containing sudoku puzzles have this same issue.
Therefore, I removed the functionality so to not clutter up the stdout output.

## License:

This codebase and project are licensed under the CC BY-NC 4.0 (Creative Commons Attribution-NonCommercial) license. For full details on sharing, adapting, and distributing,
visit this page: https://creativecommons.org/licenses/by-nc/4.0/