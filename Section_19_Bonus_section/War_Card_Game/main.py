from deck import Deck
from player import Player
from war_card_game import WarCardGame


player = Player(name="Mihael",
                deck=Deck(is_empty=True))
computer = Player(name="Computer",
                  deck=Deck(is_empty=True),
                  is_computer=True)
deck = Deck()

game = WarCardGame(player=player,
                   computer=computer,
                   deck=deck)

game.print_welcome_message()

while not game.is_game_over():
    game.play()
    game.print_statistics()
    
    next_round = input("\nDo you want to start next round?\nPress Enter to"
        + " start new round or press X to stop playing the game!")
    
    if next_round.lower() == "x":
        break