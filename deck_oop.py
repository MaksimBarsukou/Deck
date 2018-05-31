import random


class Card:
    def __init__(self, suit, rank, weight):
        """ The card class has three values, suit, rank, and card weight."""
        self.suit = suit
        self.rank = rank
        self.weight = weight

    def __repr__(self):
        """Calls the function repr to obtain formatted strings"""
        s = '{}{}:{}'.format(self.rank, self.suit, self.weight)
        return s


class Deck:
    def __init__(self):
        self.RANK = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', "A"]
        self.SUIT = ['♠', '♦', '♥', '♣']
        self.WEIGHT = {"6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
        self.deck = []
        for suit in self.SUIT:
            for rank in self.RANK:
                self.deck.append(Card(rank, suit, self.WEIGHT[rank]))
        random.shuffle(self.deck)

    @property
    def trump_card(self):
        card = self.deck[-1]
        return card

    @property
    def len_deck(self):
        size = len(self.deck)
        return size

    def trump_suit(self):
        trump_suit = '{}'.format(d.trump_card.rank)
        for i in '{}'.format(self.deck):
            if trump_suit in i:
                print(i)


        return trump_suit

    def take_card(self, numbers=6):
        card = self.deck[:numbers]
        self.deck = self.deck[numbers:]
        return card


class Hand:
    pass


d = Deck()
print(d.trump_suit())
print(d.deck)
print(d.len_deck)
print(d.take_card())
print(d.trump_card)
