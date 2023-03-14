from board import Board
from player import Player
from move import Move


class TicTacToeGame:
    
    def start(self):
        print("**************************************************")
        print("*****         Welcome to Tic-Tac-Toe         *****")
        print("**************************************************")
        
        board = Board()
        player = Player()
        computer = Player(is_human=False)
        
        board.print_board()
        
        # Ask if player wants to play another round.
        while True:
            # Get move, check tie, check game over
            while True:
                player_move = player.get_move()
                board.submit_move(player, player_move)
                board.print_board()
                
                if board.check_is_tie():
                    print("It's a tie! Try again.")
                    break
                elif board.check_is_game_over(player, player_move):
                    print("Awesome. You won the game!")
                    break
                else:
                    computer_move = computer.get_move()
                    board.submit_move(computer, computer_move)
                    board.print_board()
                    
                    if board.check_is_game_over(computer, computer_move):
                        print("Sorry, computer won! Try again.")
                        break
            
            play_again = input("Would you like to play again?" 
                               + " Enter Y for YES or N for NO: ").upper()
            
            if play_again == "N":
                print("Bye! Thank you for playing with me. :)")
                break
            elif play_again == "Y":
                self.start_new_round(board)
            else:
                print("Your input is not valid but I assume you want to play "
                      + "one more round with me!")
                self.start_new_round(board)

    def start_new_round(self, board):
        print("******************************")
        print("*****     New Round      *****")
        print("******************************")
        board.reset_board()
        board.print_board()
