from suit import Suit
from card import Card
from deck import Deck
from player import Player


# Testing Suit class
my_suit = Suit("spades")
# print(my_suit.description, my_suit.symbol)

my_card = Card(suit=my_suit, value=12)
# my_card.show()

my_deck = Deck()
# my_deck.show()
# my_deck.shuffle()
# my_deck.show()
# print(my_deck.size)
# my_deck.draw().show()
# my_deck.show()

# player = Player("Michael", my_deck)
# print(player.has_empty_deck())
# player.draw_card().show()
# player.add_card(my_card)