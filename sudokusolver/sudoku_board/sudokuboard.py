from sudoku_board.sudokucell import SudokuCell

class SudokuBoard:
    
    def __init__(self):
        # The index of each SudokuCell is referred to as its "absolute position" (as opposed to xy position)
        self.values = [SudokuCell() for _ in range(81)]
        
    def initialize_board(self, board_array):
        if len(board_array) != 81:
            raise ValueError("The initializing array for the board must be exactly length 81!")
        
        for i in range(81):
            if board_array[i] != 0:
                self.set_cell_value(board_array[i], i)
            
        
        
    # Returns integer [0-80] of absolute position of cell specified by xy coordinates    
    def coordinate_to_absolute(self, x_pos, y_pos):
        abs_pos = 9 * (y_pos - 1) + (x_pos - 1)
        return abs_pos
    
    # Returns array [x, y] for given absolute position
    def absolute_to_coordinate(self, abs_pos):
        y_pos = (abs_pos / 9) + 1
        x_pos = (abs_pos % 9) + 1
        
        return [x_pos, y_pos]
        
    # Requires a value to set a cell to. Specify one coordinate to use absolute or two coordinates to use xy.
    def set_cell_value(self, value, abs_pos, y_pos = None):
                
        if y_pos == None: # Mode 1: define an absolute position
            if abs_pos < 0 or abs_pos >= len(self.values):
                raise IndexError("Absolute position must be between 0 and 80")                
            
        else: # Mode 2: define an xy position (where [x,y] of top-left cell is [1,1] and bottom right is [9,9])
            if (abs_pos < 1 or abs_pos > 9):
                raise IndexError("x-position must be between 1 and 9 inclusive!")
            elif (y_pos < 1 or y_pos > 9):
                raise IndexError("y-position must be between 1 and 9 inclusive!")
            else:
                abs_pos = self.coordinate_to_absolute(abs_pos, y_pos)
        
        if value == -1:
            return self.values[abs_pos]        
        else:
            self.values[abs_pos].set_value(value)
        
    def get_cell_value(self, abs_pos, y_pos = None):
        return self.set_cell_value(-1, abs_pos, y_pos)
    
    def print(self):
        for i in range(81):
            self.values[i].print()
            print(" ", end="")
            if i % 3 == 2:
                print("| ", end="")
            if i % 9 == 8:
                print()
            if i % 27 == 26:
                print("-----------------------")
            
        
                
                
                
            


            
        
# class SudokuBox:
    
#     def __init__(self, initial_cells = None):
#         if initial_cells == None:
#             self.cells = [SudokuCell() for _ in range(9)]
#         else:
#             self.cells = initial_cells
#             while len(self.cells) < 9:
#                 (self.cells).append(SudokuCell())
            
#     def print(self):
#         for i in range(9):
#             if i % 3 == 1:
#                 print("| " + self.cells.at(i) + " |")
#             else:
#                 print(self.cells.at(i) + " ")
                
                
            
# class SudokuBoard:
#     def __init__(self, initial_boxes = None):
#         if initial_boxes == None:
#             self.boxes = [SudokuBox() for _ in range(9)]
#         else:
#             self.boxes = initial_boxes