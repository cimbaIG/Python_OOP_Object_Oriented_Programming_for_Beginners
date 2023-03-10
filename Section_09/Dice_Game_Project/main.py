from dice import Dice
from player import Player
from dice_game import DiceGame


# Create instances
# Create player die instance
player_die = Dice()
# Create computer die instance
computer_die = Dice()

# Create player
my_player = Player(player_die, is_computer=False)
# Create computer player
computer_player = Player(computer_die, is_computer=True)

# Create game instance from player instances
game = DiceGame(my_player, computer_player)
# Play the game
game.play()
