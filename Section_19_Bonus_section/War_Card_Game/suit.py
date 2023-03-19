class Suit:
    
    suits = {
        "clubs": "♣",
        "diamonds": "♦",
        "hearts": "♥",
        "spades": "♠"
    }
    
    def __init__(self, description: str):
        self._description = description.lower()
        try:
            self._symbol = Suit.suits[self._description]
        except KeyError:
            print("Legit suits are: clubs, diamonds, hearts and spades.")
        
    @property
    def description(self):
        return self._description
    
    @property
    def symbol(self):
        return self._symbol
    