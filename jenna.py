#level09 assignment



# card class
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self.rank_values[self.rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    rank_values = {
              "2" : 2,
              "3" : 3,
              "4" : 4,
              "5" : 5,
              "6" : 6,
              "7" : 7,
              "8" : 8,
              "9" : 9,
              "10" : 10,
              "jack" : 11,
              "queen" : 12,
              "king" : 13,
              "ace" : 14,
        }