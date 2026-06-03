from ..models.sudoku_board import SudokuBoard

def check_row(board: SudokuBoard, abs_pos: int) -> int:
    """
    Checks the row of the cell at the given absolute position for possible values. 
    If exactly one candidate value is found, it is set to that value and 1 is returned. Otherwise, 0 is returned.
    """
    
    if board.get_cell(abs_pos).get_value() != 0:
        return 0
    
    coords = board.absolute_to_coordinate(abs_pos)
    x_pos = coords[0]
    
    for i in range(1, 10):
        board.get_cell(abs_pos).remove_possible_value(board.get_cell_value(x_pos, i))
        if len(board.get_cell(abs_pos).get_possible_values()) == 1:
            board.get_cell(abs_pos).set_value(board.get_cell(abs_pos).get_possible_values()[0])
            return 1
        
    return 0
            
def check_column(board: SudokuBoard, abs_pos: int) -> int:
    """
    Checks the column of the cell at the given absolute position for possible values. 
    If exactly one candidate value is found, it is set to that value and 1 is returned. Otherwise, 0 is returned.
    """
    
    if board.get_cell(abs_pos).get_value() != 0:
        return 0
    
    coords = board.absolute_to_coordinate(abs_pos)
    y_pos = coords[1]
    
    for i in range(1, 10):
        board.get_cell(abs_pos).remove_possible_value(board.get_cell_value(i, y_pos))
        if len(board.get_cell(abs_pos).get_possible_values()) == 1:
            board.get_cell(abs_pos).set_value(board.get_cell(abs_pos).get_possible_values()[0])
            return 1
        
    return 0

def check_box(board: SudokuBoard, abs_pos: int) -> int:
    """
    Checks the box of the cell at the given absolute position for possible values. 
    If exactly one candidate value is found, it is set to that value and 1 is returned. Otherwise, 0 is returned.
    """

    if board.get_cell(abs_pos).get_value() != 0:
        return 0
    
    coords = board.absolute_to_coordinate(abs_pos)
    x_pos, y_pos = coords
    x_pos_box = (x_pos + 2) // 3
    y_pos_box = (y_pos + 2) // 3
    
    x_pos_begin = (x_pos_box - 1) * 3 + 1
    y_pos_begin = (y_pos_box - 1) * 3 + 1
    
    for x in range(x_pos_begin, x_pos_begin + 3):
        for y in range(y_pos_begin, y_pos_begin + 3):
            board.get_cell(abs_pos).remove_possible_value(board.get_cell_value(x, y))
            if (len(board.get_cell(abs_pos).get_possible_values()) == 1):
                board.get_cell(abs_pos).set_value(board.get_cell(abs_pos).get_possible_values()[0])
                return 1
    
    return 0


def run_simple_logic(board: SudokuBoard):
    """ 
    Runs the simple logic of checking each cell's row, column, and box for possible values. 
    If a cell is found to have exactly one candidate value, it is set to that value. 
    This process is repeated until no more cells can be solved with this logic.
    Returns 1 if the board is solved, otherwise returns 0.
    """

    abs_pos = 0
    
    while abs_pos < 81:
        if check_row(board, abs_pos) == 1:
            abs_pos = 0
            continue
        if check_column(board, abs_pos) == 1:
            abs_pos = 0
            continue
        if check_box(board, abs_pos) == 1:
            abs_pos = 0
            continue
        
        abs_pos += 1
            
    for i in range(81):
        if board.get_cell_value(i) == 0:
            return 0
        
    return 1
        
        
    