from deck import Deck

# Represents one player in the game of War.
# Each player has a name and their own Deck of cards.
# The front of the card list is the top of the pile (cards are played from here),
# and the end of the list is the bottom (won cards are added here).
class Player:
    # Constructor: sets the player's name and gives them their own new Deck.
    def __init__(self, name):
        self.name = name
        self.deck = Deck()

    # Adds won cards to the bottom of the player's pile.
    def collect_cards(self, cards):
        self.deck.cards.extend(cards)

    # Returns how many cards the player currently has.
    def card_count(self):
        return len(self.deck.cards)
