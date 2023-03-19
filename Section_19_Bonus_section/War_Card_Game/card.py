from suit import Suit


class Card:
    
    special_cards = {
        11: "Jack",
        12: "Queen",
        13: "King",
        14: "Ace"
    }
    
    def __init__(self, suit: Suit, value: int):
        self._suit = suit
        self._value = value
        
    @property
    def suit(self):
        return self._suit
    
    @property
    def value(self):
        return self._value
    
    def _is_special(self):
        if self.value >= 11:
            return True
        return False
    
    def show(self):
        if self._is_special():
            print(f"{Card.special_cards[self.value]} "
                  + f"of {self.suit.description}" 
                  + f" {self.suit.symbol}")
        else:
            print(f"{self.value} "
                  + f"of {self.suit.description}" 
                  + f" {self.suit.symbol}")
