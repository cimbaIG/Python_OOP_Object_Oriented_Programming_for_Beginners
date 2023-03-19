from deck import Deck


class Player:
    
    def __init__(self, name, deck: Deck, is_computer=False):
        self.name = name
        self._deck = deck
        self._is_computer = is_computer
        
    @property
    def deck(self):
        return self._deck
    
    @property
    def is_computer(self):
        return self._is_computer
