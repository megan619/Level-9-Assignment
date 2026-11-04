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

    # Removes the top card from the player's pile and returns it.
    def play_card(self):
        return self.deck.cards.pop(0)

    # Returns how many cards the player currently has.
    def card_count(self):
        return len(self.deck.cards)

    # Returns True if the player has at least one card, False if they are out.
    def has_cards(self):
        if self.card_count() >= 1:
            return True
        else:
            return False

    # Returns a readable description of the player, e.g. "Player 1: 26 cards".
    def __str__(self):
        return f"{self.name}: {self.card_count()} cards"
