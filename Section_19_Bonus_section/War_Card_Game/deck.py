from card import Card
from suit import Suit

import random


class Deck:
    
    def __init__(self, is_empty=False):
        self._cards = []
        if not is_empty:
             self.build()
        
    @property
    def size(self):
        return len(self._cards)
    
    def build(self):
        for value in range(2, 15):
            for suit in Suit.SUITS.keys():
                self._cards.append(Card(suit=Suit(suit), value=value))
    
    def show(self):
        for card in self._cards:
            card.show()
    
    def shuffle(self):
        random.shuffle(self._cards)
    
    def draw(self):
        return self._cards.pop()
    
    def add(self, card: Card):
        self._cards.insert(0, card)