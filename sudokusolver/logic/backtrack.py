from copy import deepcopy
from ..models.sudoku_board import SudokuBoard
from .simple_logic import run_simple_logic

def get_mrv_cell(board: SudokuBoard) -> int:
    """
    Returns the absolute position of the cell with the minimum remaining values (MRV) heuristic. 
    If there are multiple cells with the same number of possible values, the first one is returned.
    If none are found, returns -1.
    """
    
    cell_list = board.get_all_cells()

    mrv_cell_abs_pos = -1
    mrv_cell_num_possible_values = 10

    for i, cell in enumerate(cell_list):
        if cell.get_value() == 0:
            if len(cell.get_possible_values()) < mrv_cell_num_possible_values and len(cell.get_possible_values()) > 0:
                mrv_cell_num_possible_values = len(cell.get_possible_values())
                mrv_cell_abs_pos = i  
                
    return mrv_cell_abs_pos

def is_board_dead(board) -> bool:
    """
    Returns True if the board is in a "dead" state, meaning that there is at least one cell with no possible values. Otherwise, returns False.
    """
    
    for cell in board.get_all_cells():
        if cell.get_value() == 0 and len(cell.get_possible_values()) == 0:
            return True
        
    return False

def backtrack(board: SudokuBoard) -> tuple[SudokuBoard, int]:
    """
    Solves the Sudoku board using backtracking search with the minimum remaining values (MRV) heuristic. 
    Returns 1 if the board is solved.
    Returns 0 if the board is solved but incorrect.
    Returns -1 if the board is unsolved.
    """
    
    snapshot_board_permanent = deepcopy(board)
    snapshot_board = deepcopy(board)
    run_simple_logic(snapshot_board)

    if snapshot_board.is_complete():
        if snapshot_board.is_correct():
            return (snapshot_board, 1)
        else: 
            return (snapshot_board, 0)
        
    if is_board_dead(snapshot_board): return (snapshot_board, -1)
    
    candidate_cell_abs_pos = get_mrv_cell(snapshot_board)
    candidate_list = snapshot_board.get_cell(candidate_cell_abs_pos).get_possible_values()

    for candidate in candidate_list:
        snapshot_board.set_cell_value(candidate, candidate_cell_abs_pos)
        
    

    return (snapshot_board, -1)