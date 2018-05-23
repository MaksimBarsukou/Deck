import random


class Card(object):
    def __init__(self, suit, rank, weight):
        self.suit = suit
        self.rank = rank
        self.weight = weight

    def __repr__(self):
        s = '{}{}:{}'.format(self.rank, self.suit, self.weight)
        return s

class Deck(object):
    def __init__(self):
        self.RANK = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', "A"]
        self.SUIT = ['♠', '♦', '♥', '♣']
        self.WEIGHT = {"6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
        self.deck = []
        for suit in self.SUIT:
            for rank in self.RANK:
                self.deck.append(Card(rank, suit, self.WEIGHT[rank]))
        random.shuffle(self.deck)

    def tramp_card(self):
        trump_card = self.deck[-1]
        return trump_card

    def __len__(self):
        return len(self.deck)

    def take_card(self):
        card = self.deck[:6]
        return card




d = Deck()
print(d.deck)
print(d.tramp_card())
print(d.__len__())
print(d.take_card())