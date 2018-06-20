import random


class Card:
    def __init__(self, suit, rank, weight=None):
        """ The card class has three values, suit, rank, and card weight."""
        self.suit = suit
        self.rank = rank
        self.weight = weight

    def __repr__(self):
        """Calls the function repr to obtain formatted strings."""
        return '{}{}'.format(self.rank, self.suit)


class Deck:
    def __init__(self):
        """Fill the self.deck using RANK, SUIT, WEIGHT and mix it.
        Create a new list and assign new weights and associated new_deck in self.deck."""
        self.RANK = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', "A"]
        self.SUIT = ['♠', '♦', '♥', '♣']
        self.WEIGHT = {"6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
        self.deck = []
        for suit in self.SUIT:
            for rank in self.RANK:
                self.deck.append(Card(suit, rank, self.WEIGHT[rank]))
        random.shuffle(self.deck)
        new_deck = []
        for card in self.deck:
            new_deck.append(self.get_card_with_weight(self.deck[-1], card))
        self.deck = new_deck

    def get_card_with_weight(self, trump, current_card):
        """Redefine weight maps adding +9 to the trump card."""
        if trump.suit == current_card.suit:
            current_card.weight = self.WEIGHT[current_card.rank] + 9
            return current_card
        current_card.weight = self.WEIGHT[current_card.rank]
        return current_card

    @property
    def trump_card(self):
        """Determine trump (just take the last card)"""
        card = self.deck[-1]
        return card

    @property
    def len_deck(self):
        """Determine the size of the deck by counting the number of cards in it."""
        size = len(self.deck)
        return size

    def take_card(self, numbers=6):
        """Fill the hand. a maximum of 6 cards.
        Make a cut through the list using the data from numbers, also update self.deck through a cut."""
        cards = self.deck[:numbers]
        self.deck = self.deck[numbers:]
        return cards


class Hand:
    def __init__(self):
        self.MAX_NUMBER_CARDS = 6
        self.MIN_NUMBER_CARDS = 0

    def get_card(self):
        pass

    def discard_card(self, hand_card):
        discard = input("\n\nEnter card number from 1 to 6 for reset: ")
        discard_card = self.check_input_info(discard)
    # Sorting and deleting
        for n in sorted(discard_card, reverse=True):
            hand_card.pop(n)

    def check_input_info(self, input_str):
        if not input_str:
            print("Do not enter anything.")
            return False
    # Redo the string in the list.
        row_values_list = input_str.split(',')
        res_list = []
        try:
            for raw_value in row_values_list:
                number_card_raw = int(raw_value)
                if self.MAX_NUMBER_CARDS < number_card_raw or self.MIN_NUMBER_CARDS > number_card_raw:
                    raise IndexError
                number_card_raw -= 1
                res_list.append(number_card_raw)
            return res_list
        except IndexError:
            print("Out of range.")
            return False
        except ValueError:
            print("You entered a letter.")
            return False


d = Deck()
h = Hand()
print(d.deck)
print(d.len_deck)
print(d.trump_card)
print(d.take_card())
print(h.get_card())
