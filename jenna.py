#level09 assignment


#how to get a random card code
import random
rank = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suit = ["Hearts", "Diamonds", "Spades", "Clubs"]

#when drawing a random card
#variable_name_here = Card(random.choice(rank), randomchoice.(suit))

# card class
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def value(self):
        if isinstance(self.rank, int):
            self.value = self.rank
        elif self.rank == "Ace":
            self.value = 1
        elif self.rank == "Jack":
            self.value = 11
        elif self.rank == "Queen":
            self.value = 12
        elif self.rank == "King":
            self.value = 13