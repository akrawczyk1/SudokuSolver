class SudokuBoard:
    
    def __init__(self):
        self.values = [0] * 81
        
    def set_value(self, value, abs_pos, y_pos = None):
        if y_pos == None: # Mode 1: define an absolute position
            if abs_pos > 0 and abs_pos < len(self.values):
                self.values[abs_pos] = value
            else:
                raise IndexError("Absolute position must be between 0 and 80")
            
        else: # Mode 2: define an xy position (where [x,y] of top-left cell is [1,1] and bottom right is [9,9])
            if (abs_pos < 1 or abs_pos > 9):
                raise IndexError("x-position must be between 1 and 9 inclusive")
                
                
            

# class SudokuCell:
    
#     def __init__(self, initial_value = 0):
#         self.value = initial_value
        
#     def print(self):
#         if self.value == 0:
#             print(" ")
#         else:
#             print(self.value)
            
        
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