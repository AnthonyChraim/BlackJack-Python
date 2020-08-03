from Card import Card, values, suits
from random import shuffle


class Deck:

    def __init__(self, num_decks=1):
        self.deck = []
        for name, value in values.items():
            for suit in suits:
                self.deck.append(Card(name, suit))
        self.deck *= num_decks
        shuffle(self.deck)

    def __str__(self):
        return "\n".join(str(x) for x in self.deck)
