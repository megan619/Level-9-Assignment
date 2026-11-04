from jenna import Card
import random

class Deck:

    #constructor
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7",
                 "8", "9", "10", "Jack", "Queen", "King"]
#a list to hold the cards in each deck
        self.cards = []

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

#shuffles the deck
    def shuffle_deck(self):
        random.shuffle(self.cards)

#draws a card for the player. 
    def draw_card(self):
        return self.cards.pop()
  