class SudokuCell:
    
    def __init__(self, initial_value = 0):
        self.value = initial_value
        
        self.possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if self.value in self.possible_values:
            self.possible_values.remove(self.value)
        
    def print(self) -> None:
        if self.value == 0:
            print(" ", end="")
        else:
            print(self.value, end="")
            
    def set_value(self, val) -> None:
        if val < 0 or val > 9:
            raise ValueError("Value of a cell must be between 1 and 9 inclusive!")
        else:
            self.value = val
            self.possible_values.clear()
            
    def get_value(self) -> int:
        return self.value
    
    def get_possible_values(self) -> list[int]:
        return self.possible_values
    
    # Returns 1 if removal successful, 0 otherwise
    def remove_possible_value(self, val) -> int:
        if val == 0:
            return 0
        if val < 1 or val > 9:
            raise ValueError("Value of a cell must be between 1 and 9 inclusive!")
        elif val in self.possible_values:
            self.possible_values.remove(val)
            return 1
        else:
            return 0
        


