class Player:
    def __init__(self, name):
        self.name = name
        self.player_cards = []

    def receive_cards(self, cards):
        self.player_cards.extend(cards)

    def play_card(self):
        return self.player_cards.pop(0)
        
    def card_count(self):
        return len(self.player_cards)

    def has_cards(self):
        if self.card_count() >= 1:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name}: {self.card_count()} cards"


