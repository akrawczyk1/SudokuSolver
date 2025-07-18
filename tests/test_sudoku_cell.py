from sudokusolver.sudoku_board.sudokucell import SudokuCell

def test_sudoku_cell_starts_empty():
    cell = SudokuCell()
    assert cell.get_value() == 0
    
def test_sudoku_cell_changes_value():
    cell = SudokuCell()
    cell.set_value(5)
    assert cell.get_value() == 5