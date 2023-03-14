class Board:
    
    EMPTY_CELL = 0
    
    def __init__(self):
        self.game_board = [[0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]]
        
    def print_board(self):
        print("\nPositions:")
        self.print_board_with_positions()
        
        print("Board:")
        # Iterate through game_board and print the current board state.
        # Iterate through all the rows.
        for row in self.game_board:
            # By default python print() function ends with new line.
            # To avoid that set end parameter as an empty string.
            print("|", end="")
            # Iterate through the columns.
            for column in row:
                if column == Board.EMPTY_CELL:
                    print("   |", end="")
                else:
                    print(f" {column} |", end="")
            print()  # New line
        print()  # New line
        
    def print_board_with_positions(self):
        print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")
        
    def submit_move(self, player, move):
        # Get a current row position entered by the player
        row = move.get_row()
        # Get a current column position entered by the player
        column = move.get_column()
        # Assign the current board value at position given by player to
        # a variable named value.
        value = self.game_board[row][column]
        
        # If the board at a given position is free, i.e. if the cell at the
        # board is empty, assign the user's choice to a given position.
        if value == Board.EMPTY_CELL:
            self.game_board[row][column] = player.marker
        # In other case tell the user that the board at the given position
        # is already used!
        else:
            print("This position is already taken. Please enter another one.")
            
    def check_is_game_over(self, player, last_move):
        # Check if any of these conditions is fulfilled. If only one condition
        # is fulfilled, the game is over and True is returned!
        return self.check_row(player, last_move) \
            or self.check_column(player, last_move) \
            or self.check_diagonal(player) \
            or self.check_antidiagonal(player) 
            
    def check_row(self, player, last_move):
        # Get row index of last move
        row_index = last_move.get_row()
        # Get the row in which the last move was played
        board_row = self.game_board[row_index]
        
        # If the total number of players marker that occur in one row is equal
        # to three, return True. This means that the game is over.
        return board_row.count(player.marker) == 3
    
    def check_column(self, player, last_move):
        # Set the column marker counter value to zero
        markers_count = 0
        # Get the last move column index value
        column_index = last_move.get_column()
        # Go through all the rows and check if the marker at the last move
        # column position is equal to player marker. If so, increment the
        # marker counter.
        for row in range(3):
            if self.game_board[row][column_index] == player.marker:
                markers_count += 1
        
        # If there are three same markers in each of columns, return True and
        # the game is over.
        return markers_count == 3
    
    def check_diagonal(self, player):
        # Set the marker counter value to zero.
        markers_count = 0
        # Go through all the rows and check those position with the same
        # row and column indices (these are diagonal values). If the marker
        # at this position is equal to players marker, increment the marker
        # counter.
        for i in range(3):
            if self.game_board[i][i] == player.marker:
                markers_count += 1
        
        # If there are three same markers in diagonal, return True and the game 
        # is over.        
        return markers_count == 3
    
    def check_antidiagonal(self, player):
        # Set the marker counter value to zero.
        markers_count = 0
        # Go through all the rows and check if marker is equal to the players. 
        # If so, increment the marker counter.
        for i in range(3):
            if self.game_board[i][2-i] == player.marker:
                markers_count += 1
        
        # If there are three equal markers in antidiagonal, the marker counter 
        # value is equal to three and True is returned. The game is over.        
        return markers_count == 3
    
    def check_is_tie(self):
        # Define empty counter.
        empty_counter = 0
        # Go through every list in every row and count all zero values. If 
        # value is zero add it to the empty counter.
        for row in self.game_board:
            empty_counter += row.count(Board.EMPTY_CELL)
        
        # If empty counter is zero, return True. This means that there are no 
        # zero values in game_board matrix, which means that game_board is full 
        # and the game is over!
        return empty_counter == 0
    
    def reset_board(self):
        # If game is tie, or player just wants to play another round, reset the 
        # board by making all game_board values equal to zero!
        self.game_board = [[0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]]        
