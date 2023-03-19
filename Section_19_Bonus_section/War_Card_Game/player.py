from deck import Deck
from card import Card


class Player:
    
    def __init__(self, name: str, deck: Deck, is_computer=False):
        self.name = name
        self._deck = deck
        self._is_computer = is_computer
        
    @property
    def deck(self):
        return self._deck
    
    @property
    def is_computer(self):
        return self._is_computer
    
    def has_empty_deck(self):
        if len(self._deck.cards) == 0:
            return True
        return False
    
    def draw_card(self):
        if not self.has_empty_deck():
            return self.deck.draw()
    
    def add_card(self, card: Card):
        self.deck.add(card)
