#!/usr/bin/python
# -*- coding: <encoding name> -*-
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
        else:
            return 0

    def discard_card(self, discard_card):  # Подумать как исправить проблему(если аргументом передается
        """Remove the card number that entered the user."""  # str обьект "end", возможно сделать проверку через
        # Sorting and deleting                               #  try / except TypeError конструкцию)
        return self.hand.pop(discard_card)

    def check_input_info(self):
        """Enter the card number to delete, and check the data so that
        they do not go beyond the list and to enter the number."""
        while True:
            try:
                input_str = input("\n\nEnter card number or the word 'end' ")
                if not input_str:
                    print("Do not enter anything.")
                    continue
                if input_str == "end":
                    return "end"
                for raw_value in input_str:
                    number_card_raw = int(raw_value)
                    if len(self.hand) < number_card_raw or MIN_NUMBER_CARDS > number_card_raw:
                        raise IndexError
                    number_card_raw -= 1
                return number_card_raw
            except IndexError:
                print("Out of range.")
            except ValueError:
                print("You entered a letter.")


# --------------------------------------------------------------------------------------------------

class Table:
    def __init__(self):
        """Initialize the variables for the playing field."""
        self.deck = Deck()
        self.card_storage = []  # Storage 1 game turn (12 cards maximum)
        self.battle_repository = []  # Temporary storage of 1 battle
        self.my_hand = Hand(self.deck.trump_card)
        self.bot_hand = Hand(self.deck.trump_card)

    def first_move_on_table(self):
        player = self.my_hand.check_trump()
        bot = self.bot_hand.check_trump()
        if player == bot:
            first_move = True, False
            return random.choice(first_move)
        else:
            if player > bot:
                return True
            else:
                return False

    def check_card_on_table(self, inpt):  # порверяет что игрок отбился корректной картой
        first_card = self.battle_repository[0]
        second_card = self.my_hand.hand[inpt]
        trump_card_check = self.deck.trump_card
        if first_card.suit == second_card.suit:
            if first_card.weight < second_card.weight:
                return True
            else:
                return False
        else:
            if second_card.suit == trump_card_check.suit:
                return True
            else:
                return False

    def update_hand(self):
        """Update card in hand"""
        self.my_hand.hand += self.deck.take_card(self.my_hand.card_replenishment())
        self.my_hand.hand = sorted(self.my_hand.hand, key=lambda x: x.weight)
        self.bot_hand.hand += self.deck.take_card(self.bot_hand.card_replenishment())
        self.bot_hand.hand = sorted(self.bot_hand.hand, key=lambda x: x.weight)

    def append_and_clear_bot_hand(self, card):
        """Append and clear: battle repository and card storage in bot hand"""
        self.battle_repository.append(card)
        self.bot_hand.hand.remove(card)
        self.card_storage += self.battle_repository
        self.battle_repository.clear()
        print("{} {}".format("Карты на столе.", self.card_storage))

    def append_and_clear_player_hand(self, player_input):
        """Append and clear: battle repository and card storage in player hand"""
        self.battle_repository.append(player_input)
        self.card_storage += self.battle_repository
        self.battle_repository.clear()
        print("{} {}".format("Карты на столе.", self.card_storage))

    def what_the_player_threw(self, inpt):
        x = True
        while x:
            checked_card = [self.my_hand.hand[inpt]]
            for card in checked_card:
                for cards in self.card_storage:
                    if card.rank == cards.rank:
                        x = True
                        break
                    else:
                        x = False
            return x

    def bot_beats_cards(self):  # бот бьет карты подкинутые игроком
        while True:
            j = self.battle_repository[0]
            for card in self.bot_hand.hand:
                if card.suit == j.suit:
                    if card.weight > j.weight:
                        self.append_and_clear_bot_hand(card)
                        return True
                    else:
                        if card.suit == self.deck.trump_card.suit:
                            self.append_and_clear_bot_hand(card)
                            return True
                else:
                    if card.suit == self.deck.trump_card.suit:
                        self.append_and_clear_bot_hand(card)
                        return True
            else:
                return False

    def can_the_player_throw(self):  # проверяет может ли игрок подкинуть карту
        while True:
            for card in self.card_storage:
                for cards in self.my_hand.hand:
                    if card.rank == cards.rank:
                        return True
            else:
                return False

    def player_logic(self):  # Games logic of the player.
        """Player logic in one turn"""
        y = True
        while y:
            print("{} {}".format("Ваши карты", self.my_hand.hand))
            print("{}:{}".format("Карт осталось", self.deck.len_deck))
            print("{}:{}".format("Козырь", self.deck.trump_card.suit))
            x = True
            while x:
                if self.card_storage:
                    if self.can_the_player_throw():
                        print("{}".format("Вы можете подкинуть карту."))
                    else:
                        y = False
                        self.card_storage.clear()
                        self.update_hand()
                        print("{}".format("Конец хода игрока."), end='\n\n')
                        break
                inpt = self.my_hand.check_input_info()
                if inpt != "end":
                    if self.card_storage:
                        if not self.what_the_player_threw(inpt):
                            print("{}".format("Неверная карта."))
                            print("{} {}".format("Карты на столе.", self.card_storage))
                            break
                    a = self.my_hand.discard_card(inpt)
                    self.battle_repository.append(a)
                    if self.bot_beats_cards():
                        x = False
                        break
                    else:
                        self.card_storage.extend(self.battle_repository)
                        self.bot_hand.hand.extend(self.card_storage)
                        self.battle_repository.clear()
                        self.card_storage.clear()
                        self.update_hand()
                        print("{}".format("Бот не отбился и забрал карты."), end='\n\n')
                        x = False
                        break
                else:
                    print("Игрок заканчивает ход.")
                    self.battle_repository.clear()
                    self.card_storage.clear()
                    self.update_hand()
                    print(self.my_hand.hand)
                    print(self.bot_hand.hand)
                    y = False
                    break

    def throws_cards(self):  # Check what cards can  throw.
        while True:
            for card in self.card_storage:
                for cards in self.bot_hand.hand:
                    if card.rank == cards.rank:
                        self.battle_repository.append(cards)
                        self.bot_hand.hand.remove(cards)
                        print("{} {}".format("Бот кладёт карту.", self.battle_repository[0]), end='\n\n')
                        return True
            else:
                return False

    def bot_logic(self):  # Games logic of the bot.
        """Bot logic in one turn"""
        x = True
        while x:
            self.battle_repository.clear()
            bot_card = self.bot_hand.hand[0]
            self.battle_repository.append(bot_card)
            self.bot_hand.hand.remove(bot_card)
            print("{} {}".format("Бот кладёт карту.", self.battle_repository[0]))
            print("{}:{}".format("Ваши карты", self.my_hand.hand))
            z = True
            while z:
                print("{}:{}".format("Карт осталось", self.deck.len_deck))
                print("{}:{}".format("Козырь", self.deck.trump_card.suit))
                card_player_input = self.my_hand.check_input_info()
                if card_player_input != "end":
                    x = self.check_card_on_table(card_player_input)
                    if x is True:
                        player_card = self.my_hand.discard_card(card_player_input)
                        self.append_and_clear_player_hand(player_card)
                        y = True
                        while y:
                            if self.throws_cards():
                                print("{}:{}".format("Ваши карты", self.my_hand.hand))
                                y = False
                                break
                            else:
                                print("{}".format("Конец хода."), end='\n\n')
                                z = False
                                x = False
                                self.update_hand()
                                self.card_storage.clear()
                                break
                    else:
                        print("{}".format("Неверная карта.", end='\n\n'))
                        print("{} {}".format("Бот кладёт карту.", self.battle_repository[0]))
                        print("{}:{}".format("Ваши карты", self.my_hand.hand))
                        print("{} {}".format("Карты на столе.", self.card_storage))
                else:
                    if self.battle_repository:
                        self.card_storage.extend(self.battle_repository)
                        self.my_hand.hand.extend(self.card_storage)
                        self.battle_repository.clear()
                        self.card_storage.clear()
                        self.update_hand()
                        print("{}".format("Вы забираете карты."))

                        break
                    else:
                        print("{}".format("Вы пополняете руку."))
                        self.card_storage.clear()
                        self.update_hand()
                        print("{}:{}".format("Ваши карты", self.my_hand.hand))
                        x = False
                        break


# --------------------------------------------------------------------------------------------------

class game():
    def main(self):
        t = Table()
        t.update_hand()
        d = Deck()
        x = d.len_deck
        if t.first_move_on_table():
            while x > 0:
                t.player_logic()
                t.bot_logic()
        else:
            while x > 0:
                t.bot_logic()
                t.player_logic()


if __name__ == '__main__':
    game().main()
