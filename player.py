from deck import Deck

# Represents one player in the game of War.
# Each player has a name and their own Deck of cards.
# The end of the card list is the top of the pile (Deck's draw_card takes from here),
# and the front of the list is the bottom (won cards are added here).
class Player:
    # Constructor: sets the player's name and gives them their own new Deck.
    def __init__(self, name):
        self.name = name
        self.deck = Deck()

    # Adds won cards to the bottom of the player's pile (the front of the list),
    # so they aren't drawn again right away.
    def collect_cards(self, cards):
        import random
        random.shuffle(cards)
        self.deck.cards = cards + self.deck.cards

    # Returns how many cards the player currently has.
    def card_count(self):
        return len(self.deck.cards)
