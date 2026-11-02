from jenna import Card
import random

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7",
                 "8", "9", "10", "Jack", "Queen", "King"]

        self.cards = []

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if self.cards == []:
                return None
        else:
                return self.cards.pop()
  