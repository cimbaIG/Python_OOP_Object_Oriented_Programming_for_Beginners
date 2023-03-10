class DiceGame:
    
    def __init__(self, player, computer):
        self._player = player
        self._computer = computer
        
    # There will no be getters or setters for this class attributes
    # as they should be completely non-public and should not be used
    # outside the class.
    
    def play(self):
        print("===========================================")
        print("  🎲🎲🎲  Welcome to Roll the Dice!  🎲🎲🎲  ")
        print("===========================================")
        
        while True:
            self._play_round()
            game_over = self._check_game_over()
            if game_over:
                break
            
    def _play_round(self):
        # Welcome the player
        self._print_round_welcome()
        
        # Roll the dice
        # Player rolling the dice...
        self._player.roll_dice()
        # Computer rolling the dice
        self._computer.roll_dice()
        
        # Show the values of dice rolling
        self._show_dice(self._player._dice._value, 
                        self._computer._dice._value)
        
        # Determine winner and loser
        if self._player._dice._value > self._computer._dice._value:
            print("🎉🎉🎉 You won the round! 🎉🎉🎉")
            self._update_counters(winner=self._player, 
                                 loser=self._computer)
        elif self._computer._dice._value > self._player._dice._value:
            print("😿😿😿 The computer won this round. Try again. 😿😿😿")
            self._update_counters(winner=self._computer,
                                 loser=self._player)
        else:
            print("😎😎😎 It's a tie! 😎😎😎")
        
        self._show_counters()
        print("-----------------------------------------")

    def _print_round_welcome(self):
        print("\n---------------- New Round ----------------")
        # Press any key to roll the dice using input() function
        input(" 🎲🎲  Press any key to roll the dice.  🎲🎲 ")

    def _show_dice(self, player_value, computer_value):
        print(f"Your dice: {player_value}")
        print(f"Computer dice: {computer_value}\n")        
        
    def _update_counters(self, winner, loser):
        winner.decrement_counter()
        loser.increment_counter()
    
    def _show_counters(self):
        # Show counter values for the player and computer   
        print(f"\nYour counter: {self._player.counter}")
        print(f"Computer counter: {self._computer.counter}")

    def _check_game_over(self):
        if self._player.counter == 0:
            self._show_game_over(self._player)
            return True
        elif self._computer.counter == 0:
            self._show_game_over(self._computer)
            return True
        else:
            return False
        
    def _show_game_over(self, winner):
        print("\n===========================================")
        if winner.is_computer:
            print("                GAME OVER!                ")
            print("===========================================")
            print("        The computer won the game.         ")
        else:
            print("                GAME OVER!                ")
            print("===========================================")
            print("    You won the game. Congratulations!     ")
        print("===========================================")
