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
        return '{}{}:{}'.format(self.rank, self.suit, self.weight)


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
            new_deck.append(self.get_card_with_weight(self.trump_card, card))
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
    def __init__(self, trump):
        """Initialize an empty hand and a trump card for convenience."""
        self.hand = []
        self.trump = trump

    def check_trump(self):
        """We check the cards in the hand for the presence of trump cards, then find the highest trump."""
        a = []
        for card in self.hand:
            if self.trump.suit == card.suit:
                a.append(card.weight)
        len_a = len(a)
        if not a:
            return 0
        elif len_a == 1:
            return a[0]
        else:
            x = max(a)
            return x

    def card_replenishment(self):
        """Count the number of missing cards in your hand."""
        len_hand = len(self.hand)
        if len_hand < MAX_NUMBER_CARDS:
            missing_cards = MAX_NUMBER_CARDS - len_hand
            return missing_cards

    def discard_card(self, discard_card):
        """Remove the card number that entered the user."""
        # Sorting and deleting
        if discard_card != 'end':
            for x in discard_card:
                return self.hand.pop(x)
        else:
            return 'end'

    def check_input_info(self):
        """Enter the card number to delete, and check the data so that
        they do not go beyond the list and to enter the number."""
        while True:
            try:
                input_str = input("\n\nEnter card number or the word 'end' ")
                if not input_str:
                    print("Do not enter anything.")
                    continue
                if input_str == 'end':
                    return 'end'
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


# --------------------------------------------------------------------------------------------------

class Table:
    def __init__(self):
        """Initialize the variables for the playing field."""
        self.deck = Deck()
        # Так как Hand требует trump для работы  обсчета козырных карт то инициализируем self.hand из класса Hand
        #  и передаем в него  козырь
        self.card_storage = []  # хранилище 1 игрового хода( 12 карт максимум)
        self.battle_repository = []  # временное хранилище 1 боя
        self.my_hand = Hand(self.deck.trump_card)
        self.bot_hand = Hand(self.deck.trump_card)

    def first_move(self):
        player = self.my_hand.check_trump()
        bot = self.bot_hand.check_trump()
        if player == bot:
            first_move = 'player', 'bot'
            return random.choice(first_move)
        else:
            if player > bot:
                return 'player'
            else:
                return 'player'

    def check_card_on_table(self):
        first_card = self.battle_repository[0]
        second_card = self.battle_repository[1]
        if first_card.suit == second_card.suit:
            if first_card.weight < second_card.weight:
                self.card_storage.extend(self.battle_repository)
                self.battle_repository.clear()
                return "Beat"
            else:
                return "Less value"
        else:
            return "Improper card suit"

    def start_game(self):
        self.my_hand.hand = sorted(self.deck.take_card(6), key=lambda x: x.weight)
        print(self.my_hand.hand)
        self.bot_hand.hand = sorted(self.deck.take_card(6), key=lambda x: x.weight)
        print(self.bot_hand.hand)
        if self.first_move() == 'player':
            while len(self.my_hand.hand) != 0:
                inp = self.my_hand.check_input_info()
                if inp == 'end':
                    print('End')
                    self.my_hand.hand += self.deck.take_card(self.my_hand.card_replenishment())
                    print(self.my_hand.hand)
                    self.bot_hand.hand += self.deck.take_card(self.bot_hand.card_replenishment())
                    print(self.bot_hand.hand)
                    break
                a = self.my_hand.discard_card(inp)
                self.battle_repository.append(a)
                j = self.battle_repository[0]
                for card in self.bot_hand.hand:
                    if card.suit == j.suit:
                        print('совпадает')
                        if card.weight > j.weight:
                            self.bot_hand.hand.remove(card)
                            self.battle_repository.append(card)
                            print('ранк больше')
                            self.card_storage += self.battle_repository
                            self.battle_repository.clear()
                            print(self.my_hand.hand)
                            print(self.bot_hand.hand)
                            print("card storage", t.card_storage)
                            print("battle repository", t.battle_repository)
                            break
                        else:
                            if card.suit == self.deck.trump_card.suit:
                                self.battle_repository.append(card)
                                self.bot_hand.hand.remove(card)
                                self.card_storage += self.battle_repository
                                self.battle_repository.clear()
                                print(self.my_hand.hand)
                                print(self.bot_hand.hand)
                                print("card storage", t.card_storage)
                                print("battle repository", t.battle_repository)
                                break
                    else:
                        if card.suit == self.deck.trump_card.suit:
                            self.battle_repository.append(card)
                            self.bot_hand.hand.remove(card)
                            self.card_storage += self.battle_repository
                            self.battle_repository.clear()
                            print(self.my_hand.hand)
                            print(self.bot_hand.hand)
                            print("card storage", t.card_storage)
                            print("battle repository", t.battle_repository)
                            break


t = Table()
print(t.deck.trump_card)
print(t.start_game())
print("card storage", t.card_storage)
print("battle repository", t.battle_repository)
