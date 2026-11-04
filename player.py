from deck import Deck

class Player:
    def __init__(self, name):
        self.name = name
        self.deck = Deck()

    def collect_cards(self, cards):
        self.deck.cards.extend(cards)

    def play_card(self):
        return self.deck.cards.pop(0)
        
    def card_count(self):
        return len(self.deck.cards)

    def has_cards(self):
        if self.card_count() >= 1:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name}: {self.card_count()} cards"


