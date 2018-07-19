import random

MAX_NUMBER_CARDS = 6
MIN_NUMBER_CARDS = 0


class Card:
    def __init__(self, suit, rank, weight=None):
        """ The card class has three values, suit, rank, and card weight."""
        self.suit = suit
        self.rank = rank
        self.weight = weight

    def __repr__(self):
        """Calls the function repr to obtain formatted strings."""
        return '{}{}'.format(self.rank, self.suit)


# ----------------------------------------------------------------------------------------------------


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

    def take_card(self, numbers):
        """Fill the hand. a maximum of 6 cards.
        Make a cut through the list using the data from numbers, also update self.deck through a cut."""
        cards = self.deck[:numbers]
        self.deck = self.deck[numbers:]
        return cards


# --------------------------------------------------------------------------------------------------


class Hand:
    def __init__(self):
        self.hand = []
        self.trump = Deck.trump_card

    def check_trump(self, current_hand):
        for card in current_hand:
            if self.trump.trump_card.suit == card.suit:
                weight_card = max(card.weight)
                return weight_card

    def card_replenishment(self):
        len_hand = len(self.hand)
        if len_hand < MAX_NUMBER_CARDS:
            missing_cards = MAX_NUMBER_CARDS - len_hand
            return missing_cards

    def discard_card(self):
        discard_card = self.check_input_info()
        # Sorting and deleting
        for x in discard_card:
            self.hand.pop(x)

    def check_input_info(self):
        while True:
            try:
                input_str = input("\n\nEnter card number from 1 to 6 for reset: ")
                if not input_str:
                    print("Do not enter anything.")
                    continue
                res_list = []
                for raw_value in input_str:
                    number_card_raw = int(raw_value)
                    if MAX_NUMBER_CARDS < number_card_raw or MIN_NUMBER_CARDS > number_card_raw:
                        raise IndexError
                    number_card_raw -= 1
                    res_list.append(number_card_raw)
                return res_list
            except IndexError:
                print("Out of range.")
            except ValueError:
                print("You entered a letter.")


class Table:

    def __init__(self):
        self.deck = Deck()
        self.my_hand = Hand()
        self.bot_hand = Hand()

    # def test(self):
    #     print(self.my_hand.hand)
    #     print(self.bot_hand.hand)
    #     self.my_hand.hand = self.deck.take_card(6)
    #     print("v kolode ostalos 1: ", self.deck.len_deck)
    #     self.bot_hand.hand = self.deck.take_card(6)
    #     print("v kolode ostalos 2: ", self.deck.len_deck)
    #     print("my hand under discard")
    #     print(self.my_hand.hand)
    #     self.my_hand.discard_card()
    #     print("my hand after discard")
    #     print(self.my_hand.hand)
    #     print("bot hand under discard")
    #     print(self.bot_hand.hand)
    #     self.bot_hand.discard_card()
    #     print("bot hand after discard")
    #     print(self.bot_hand.hand)

    def start_game(self):
        self.my_hand = self.deck.take_card(6)
        print(self.my_hand)
        print(self.deck.len_deck)
        self.bot_hand = self.deck.take_card(6)
        print(self.bot_hand)
        print(self.deck.len_deck)
        bot_weight_trump = Hand.check_trump(self.bot_hand)
        player_weight_trump = Hand.check_trump(self.my_hand)
        if bot_weight_trump > player_weight_trump:
            print("First move Bot")
        else:
            print("First move player")

d = Deck()
h = Hand()
t = Table()
# print(d.deck)
# print(d.len_deck)
# print(d.trump_card)
# print(d.take_card(6))
# print(d.len_deck)
# print(h.check_input_info())
# t.test()
print(t.start_game())
