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

    def check_trump(self, hand):
        """We check the cards in the hand for the presence of trump cards, then find the highest trump."""
        a = []
        for card in hand:
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

    def discard_card(self, discard_card, current_hand):
        """Remove the card number that entered the user."""
        # Sorting and deleting
        for x in discard_card:
            return current_hand.pop(x)

    def check_input_info(self):
        """Enter the card number to delete, and check the data so that
        they do not go beyond the list and to enter the number."""
        while True:
            try:
                input_str = input("\n\nEnter card number for reset: ")
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
        self.hand = Hand(self.deck.trump_card)
        self.card_storage = []
        self.battle_repository = []
        self.my_hand = Hand(self.deck.trump_card)
        self.bot_hand = Hand(self.deck.trump_card)

    # переделать функцию
    def first_move(self):
        player = self.hand.check_trump(self.my_hand)
        bot = self.hand.check_trump(self.bot_hand)
        if player == bot:
            first_move = list(player, bot)
            return random.choice(first_move)
        else:
            if player > bot:
                return 'player'
            else:
                return 'bot'

    def check_card_on_table(self):
        first_card = self.battle_repository[0]
        second_card = self.battle_repository[1]
        if first_card.suit == second_card.suit:
            if first_card.weight < second_card.weight:
                self.card_storage.extend(self.battle_repository)
                self.card_storage.clear()
                return "Beat"
            else:
                return "Less value"
        else:
            return "Improper card suit"


    def start_game(self):
        self.my_hand = self.deck.take_card(6)
        print(self.my_hand)
        self.bot_hand = self.deck.take_card(6)
        if self.first_move() == 'player':
            a = self.hand.discard_card(self.hand.check_input_info(), self.my_hand)
            print(self.my_hand)
            self.battle_repository.append(a)
            j = self.battle_repository[0]
            for card in self.bot_hand:
                if card.suit == j.suit:
                    print('совпадает')
                    if card.rank > j.rank:
                        print('ранк больше', card.rank)

        # Если ходит игрок: показать игроку его руку и предложить право первого хода. если ход втрой предлагаем выбор
        # забрать или бится если забрать то сливаем батл репоситори в руку игрока, если бой то  предлагаем выбрать
        # карту попутно проверяем её на то что она соответсвует масти покрываемой карты и также что она больше её, иначе
        # уведомляем о том что карта не та и повторно вызываем выбор карты.
        # Если ходит бот: выбираем самую меньшую карту из руки не казырную. если бьется сверяем масть покрываемой карты
        # с картами руки если мась совадает выбираем большую карту чем покрываемая на 1 значение, если масть не
        # совпадает проверяем руку на наличие козыря и выбирает наименьшую из них.
        # P.S набросать метод первого хода бота и игрока в функции старт гейм, показать только руку игрока, руку бота
        #  скрыть, показать козырью, если хоит игрок дать право выбора карты( набросать функцию проверки покрываемой
        #  карты  игроком.


t = Table()
print(t.deck.trump_card)
print(t.start_game())
print("card storage", t.card_storage)
print("battle repository", t.battle_repository)