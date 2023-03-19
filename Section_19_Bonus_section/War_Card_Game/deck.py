from card import Card
from suit import Suit

import random


class Deck:
    
    def __init__(self, cards=None):
        if cards is None:
            self._cards = []
        else:
            self._cards = cards
        self._size = len(self._cards)
        
    @property
    def size(self):
        return self._size
    
    def build(self):
        for value in range(2, 15):
            for suit in Suit.suits.keys():
                self._cards.append(Card(suit=Suit(suit), value=value))
    
    def show(self):
        for card in self._cards:
            card.show()
    
    def shuffle(self):
        random.shuffle(self._cards)
    
    def draw(self):
        pass
    
    def add(self):
        pass