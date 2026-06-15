from .sudoku_cell import SudokuCell

class SudokuBoard:
    
    def __init__(self) -> None:
        # The index of each SudokuCell is referred to as its "absolute position" (as opposed to xy position)
        self.values = [SudokuCell() for _ in range(81)]
        
    def initialize_board(self, board_array) -> None:
        if len(board_array) != 81:
            raise ValueError("The initializing array for the board must be exactly length 81!")
        
        for i in range(81):
            if board_array[i] != 0:
                self.set_cell_value(board_array[i], i)   
            
    # Returns integer [0-80] of absolute position of cell specified by xy coordinates    
    def coordinate_to_absolute(self, x_pos, y_pos) -> int:
        abs_pos = 9 * (y_pos - 1) + (x_pos - 1)
        return abs_pos
    
    # Returns array [x, y] for given absolute position
    def absolute_to_coordinate(self, abs_pos) -> list[int]:
        y_pos = (abs_pos // 9) + 1
        x_pos = (abs_pos % 9) + 1
        
        return [x_pos, y_pos]
    
    def get_cell(self, abs_pos) -> SudokuCell:
        return self.values[abs_pos]
    
    def get_all_cells(self) -> list[SudokuCell]:
        return self.values
    
    def get_all_values(self) -> list[int]:
        ret_list = []
        for cell in self.values:
            ret_list.append(cell.get_value())

        return ret_list
        
    # Requires a value to set a cell to. Specify one coordinate to use absolute or two coordinates to use xy.
    def set_cell_value(self, value, abs_pos_or_x_pos, y_pos = None):
                        
        if y_pos == None: # Mode 1: define an absolute position
            abs_pos = abs_pos_or_x_pos
            if abs_pos < 0 or abs_pos >= len(self.values):
                raise IndexError("Absolute position must be between 0 and 80")                
            
        else: # Mode 2: define an xy position (where [x,y] of top-left cell is [1,1] and bottom right is [9,9])
            x_pos = abs_pos_or_x_pos
            if (x_pos < 1 or x_pos > 9):
                raise IndexError("x-position must be between 1 and 9 inclusive!")
            elif (y_pos < 1 or y_pos > 9):
                raise IndexError("y-position must be between 1 and 9 inclusive!")
            else:
                abs_pos = self.coordinate_to_absolute(x_pos, y_pos)
                      
        self.values[abs_pos].set_value(value)

    # Requires one coordinate to use absolute or two coordinates to use xy.    
    def get_cell_value(self, abs_pos_or_x_pos, y_pos = None) -> int:
        if y_pos == None:
            abs_pos = abs_pos_or_x_pos
            return self.get_cell(abs_pos).get_value()
        else:
            x_pos = abs_pos_or_x_pos
            return self.get_cell(self.coordinate_to_absolute(x_pos, y_pos)).get_value()
        
    def is_compatible_with(self, original_board) -> int:
        for i in range(0, 81):
            if original_board.get_cell_value(i) != 0:
                if original_board.get_cell_value(i) != self.get_cell_value(i):
                    return 0
                
        return 1

    def is_complete(self) -> int:
        """
        Checks if the board contains any empty cells. Returns 1 if it is complete, otherwise returns 0.
        """

        for i in range(81):
            if self.get_cell_value(i) == 0:
                return 0
            
        return 1
        
    def is_correct(self) -> int:
        """
        Checks if the board is solved correctly by iterating across every row, column, and box. 
        Returns 1 if it is, otherwise returns 0.
        """

        col_arr = []
        for x in range(1, 10):
            for y in range(1, 10):
                col_arr.append(self.get_cell_value(x, y))
                
            col_arr.sort()
            for i in range(9):
                if col_arr[i] != (i + 1):
                    return 0
                
            col_arr.clear()
                
        row_arr = []
        for y in range(1, 10):
            for x in range(1, 10):
                row_arr.append(self.get_cell_value(x, y))
                
            row_arr.sort()
            for i in range(9):
                if row_arr[i] != (i + 1):
                    return 0
                
            row_arr.clear()

        box_arr = []
        for x in range(1, 10, 3):
            for y in range(1, 10, 3):
                for x_box in range(x, x + 3):
                    for y_box in range(y, y + 3):
                        box_arr.append(self.get_cell_value(x_box, y_box))
                        
                box_arr.sort()
                for i in range(9):
                    if box_arr[i] != (i + 1):
                        return 0
                    
                box_arr.clear()

        return 1
    
    def print(self) -> None:
        for i in range(81):
            self.values[i].print()
            print(" ", end="")
            if i % 3 == 2:
                print("| ", end="")
            if i % 9 == 8:
                print()
            if i % 27 == 26:
                print("-----------------------")
            