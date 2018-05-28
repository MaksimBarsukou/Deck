import random


class Card:
    def __init__(self, suit, rank, weight):
        self.suit = suit
        self.rank = rank
        self.weight = weight

    def __repr__(self):
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

    def trump_card(self):
        trump_card = self.deck[-1]
        return trump_card
    trump = property(trump_card)

    def len_deck(self):
        return len(self.deck)
    len = property(len_deck)

    def take_card(self):
        card = self.deck[:6]
        self.deck = self.deck[6:]
        return card


class Hand:
    pass


d = Deck()
print()
print(d.deck)
print(d.trump)
print(d.len)
print(d.take_card())
print(d.deck)
print(d.len)
