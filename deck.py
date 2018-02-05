# Подключаем модуль рандома.
import random

# Создаем список карт.


RANKS = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', "A"]
SUITS = ['♠', '♦', '♥', '♣']
WEIGHT = {"6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
MAX_NUMBER_CARDS = 6
MIN_NUMBER_CARDS = 0
deck = [r + s for r in RANKS for s in SUITS]
print(deck)

print("Всего карт в колоде: ", len(deck))
# Перемешиваем колоду.
# random.shuffle(deck)

# Возвращаем случайный элемент списка, который будет козырем.
random_deck = random.choice(deck)

# Определяем индекс козыря.Default task
trump = deck.index(random_deck)

# Удаляем по индексу элемент для переноса в конец списка.
deck.pop(trump)

# Добавляем в конец списка из Trump вырезанный элемент.
deck.append(random_deck)

# Выводим козырь.
print("Козырь объявлен: ", random_deck)

# First distribution
hand = deck[0:6]
for elem in hand:
    print(elem, end='.')
deck = deck[6:]
# Second
hand_ii = deck[0:6]
deck = deck[6:]
# firs move ii
#print("\nКомпьютер ходит: ", min(hand_ii))


def fill_hand(deck_in, hand_in, count_card_in):
    # немного не верно так делать, но позже переделаешь
    # Пополнение руки новыми картами
    new_hand = hand_in + deck_in[:count_card_in]
    # Переделываем список в строку
    new_deck = deck_in[count_card_in:]
    return new_deck, new_hand


def check_input_info(input_str):
    # Переделываем строку в список
    if not input_str:
        print("Ты ничего не ввел")
        return False
    # Переделываем строку в список

    row_values_list = input_str.split(',')
    res_list = []
    try:
        for raw_value in row_values_list:
            number_card_raw = int(raw_value)
            if MAX_NUMBER_CARDS < number_card_raw or MIN_NUMBER_CARDS > number_card_raw:
                raise IndexError
            number_card_raw -= 1
            res_list.append(number_card_raw)
        return res_list
    except IndexError:
        print("Выход за пределы")
        return False
    except ValueError:
        print("Введена буква")
        return False


while deck:
    # Запрос на сброс карт
    g = input("\n\nВыберите номера карт от 1 до 6 через , для сброса: ")
    numbers_card_del = check_input_info(g)
    if not numbers_card_del:
        continue
    # Сортировка и удаление карт
    for n in sorted(numbers_card_del, reverse=True):
        hand.pop(n)
    print("Ложу:",hand.pop(n))
    Y = "y"
    answer = str(input("Отбой y:"))
    if answer == Y:
        print("Отбой")

    count_card = len(numbers_card_del)
    deck, hand = fill_hand(deck, hand, count_card)
    for elem in hand:
        print(elem, end=' . ')
    print("\nОсталось карт: ", len(deck))