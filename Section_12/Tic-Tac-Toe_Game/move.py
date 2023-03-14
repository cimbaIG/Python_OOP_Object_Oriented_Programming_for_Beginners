class Move:
    
    def __init__(self, value):
        self._value = value
    
    # Getter (we want it to be read-only property and this is the reason
    # why we do not implement the)
    @property
    def value(self):
        return self._value
    
    # Check if move is a number between 1 and 9 (both inclusive)
    def is_valid(self):
        return 1 <= self._value <= 9
    
    def get_row(self):
        # First row
        if self._value in (1, 2, 3):
            return 0 
        # Second row
        elif self._value in (4, 5, 6):
            return 1 
        # Third row
        else:
            return 2 
    
    def get_column(self):
        # First column
        if self._value in (1, 4, 7):
            return 0
        # Second column
        elif self._value in (2, 5, 8):
            return 1
        # Third column
        else:
            return 2
   