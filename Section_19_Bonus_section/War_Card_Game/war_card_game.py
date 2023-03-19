from deck import Deck
from player import Player


class WarCardGame:
    
    def __init__(self, player: Player, computer: Player, deck: Deck):
        self._player = player
        self._computer = computer
        self._deck = deck
