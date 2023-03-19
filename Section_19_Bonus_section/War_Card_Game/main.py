from suit import Suit
from card import Card
from deck import Deck


# Testing Suit class
my_suit = Suit("spades")
# print(my_suit.description, my_suit.symbol)

my_card = Card(suit=my_suit, value=12)
# my_card.show()

my_deck = Deck()
my_deck.build()
my_deck.show()
my_deck.shuffle()
my_deck.show()
my_deck.draw().show()
my_deck.show()