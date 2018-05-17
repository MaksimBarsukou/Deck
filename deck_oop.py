import random


class Card:
    rank = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', "A"]
    suits = ['♠', '♦', '♥', '♣']
    weight = {"6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}


class Deck(Card):
    stack = [r + s for r in Card.rank for s in Card.suits]  # create a deck of rank and suits
    random.shuffle(stack)


print(Deck.stack)
print(len(Deck.stack))


class Hand(Deck):
    min_size_hand = 0
    max_size_hand = 6
    hand = Deck.stack[0:6]  # cut deck for first distribution
    #Deck.stack = Deck.stack[6:]


print(Hand.hand)
print(Deck.stack)
