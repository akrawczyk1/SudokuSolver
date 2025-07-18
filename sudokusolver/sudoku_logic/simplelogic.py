from sudoku_board.sudokuboard import SudokuBoard

def check_row(board: SudokuBoard, abs_pos: int) -> int:
    # cell = board.get_cell(abs_pos)
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
    # cell = board.get_cell(abs_pos)
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
    # cell = board.get_cell(abs_pos)
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

def check_board(board: SudokuBoard) -> int:
    
    row_arr = []
    for x in range(1, 10):
        for y in range(1, 10):
            row_arr.append(board.get_cell_value(x, y))
            
        row_arr.sort()
        for i in range(9):
            if row_arr[i] != (i + 1):
                return 0
            
        row_arr.clear()
            
    col_arr = []
    for y in range(1, 10):
        for x in range(1, 10):
            col_arr.append(board.get_cell_value(x, y))
            
        col_arr.sort()
        for i in range(9):
            if col_arr[i] != (i + 1):
                return 0
            
        col_arr.clear()
            
    return 1
        
        
    