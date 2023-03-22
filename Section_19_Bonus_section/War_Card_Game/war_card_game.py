from deck import Deck
from player import Player
from card import Card


class WarCardGame:
     
    ROUND_OUTCOME = {
        "player_wins": 0,
        "computer_wins": 1,
        "tie": 2
    }
     
    def __init__(self, player: Player, computer: Player, deck: Deck):
        self._player = player
        self._computer = computer
        self._deck = deck
        self._make_initial_decks()

    def _make_initial_decks(self):
        self._deck.shuffle()
        self._make_deck(participant=self._player)
        self._make_deck(participant=self._computer)
    
    def _make_deck(self, participant: Player):
        for _ in range(26):
            participant.add_card(self._deck.draw())
    
    def _round_winner(self, player_card: Card, computer_card: Card):
        if player_card.value > computer_card.value:
            return WarCardGame.ROUND_OUTCOME["player_wins"]
        elif player_card.value < computer_card.value:
            return WarCardGame.ROUND_OUTCOME["computer_wins"]
        else:
            return WarCardGame.ROUND_OUTCOME["tie"]
    
    def _cards_won(self, players_card: Card, computers_card: Card, 
                   previous_cards: list):
        if previous_cards:
            return [players_card, computers_card] + previous_cards
        else:
            return [players_card, computers_card]
    
    def _add_cards_to_winners_deck(self, winner: Player, list_of_cards: list):
        for card in list_of_cards:
            winner.add_card(card)
    
    def _start_card_war(self, battle_cards: list):
        players_cards = []
        computers_cards = []
        
        for i in range(3):
            players_card = self._player.draw_card()
            players_cards.append(players_card)
            computers_card = self._computer.draw_card()
            computers_cards.append(computers_card)
            
        self.play(cards_from_war=players_cards + computers_cards 
                  + battle_cards)
    
    def print_statistics(self):
        print("**************************************************************")
        print(f"You have {self._player.deck.size} cards in your deck!")
        print(f"Computer has {self._computer.deck.size} cards in its deck!")
        print("**************************************************************")
    
    def print_welcome_message(self):
        print("************************************************")
        print("***************** War Card Game ****************")
        print("************************************************")
    
    def is_game_over(self):
        print("************************************************")
        print("******************* Game over! *****************")
        print("************************************************")
        if self._player.has_empty_deck():
            print("Try again. Computer won this game!")
            return True
        elif self._computer.has_empty_deck():
            print(f"{self._player.name}, congrats! You won!")
            return True
        else:
            return False
            
    def play(self, cards_from_war=None):
        print("\n*************** Let's play War of cards! ***************")
        
        players_card = self._player.draw_card()
        computers_card = self._computer.draw_card()
            
        print("Your card is ", players_card.show())
        print("Computers card is ", computers_card.show())
            
        winner = self._round_winner(players_card, computers_card)
        cards_won = self._cards_won(players_card=players_card,
                                    computers_card=computers_card,
                                    previous_cards=cards_from_war)

        if winner == WarCardGame.ROUND_OUTCOME["player_wins"]:
            print("\nYou won this round!")
            self._add_cards_to_winners_deck(winner=self._player,
                                            list_of_cards=cards_won)
        elif winner == WarCardGame.ROUND_OUTCOME["computer_wins"]:
            print("\nThe computer won this round!")
            self._add_cards_to_winners_deck(winner=self._computer,
                                            list_of_cards=cards_won)
        else:
            print("It's a tie! Let's start war of cards!")
            self._start_card_war(battle_cards=cards_won)
