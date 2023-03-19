from suit import Suit
from card import Card


# Testing Suit class
my_suit = Suit("SpAdes")
print(my_suit.description, my_suit.symbol)

my_card = Card(suit=my_suit, value=11)
my_card.show()