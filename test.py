#Подключаем модуль рандома.
import random
#Создаем список карт.
deck = ["Clubs Ace", "Clubs 2", "Clubs 3", "Clubs 4", "Clubs 5", "Clubs 6", "Clubs 7", "Clubs 8", "Clubs 9", "Clubs 10", "Clubs Jack", "Clubs Quenn", "Clubs King",
       "Diamonds Ace", "Diamonds 2", "Diamonds 3", "Diamonds 4", "Diamonds 5", "Diamonds 6", "Diamonds 7", "Diamonds 8", "Diamonds 9", "Diamonds 10", "Diamonds Jack", "Diamonds Quenn", "Diamonds King",
       "Hearts Ace", "Hearts 2", "Hearts 3", "Hearts 4", "Hearts 5", "Hearts 6", "Hearts 7", "Hearts 8", "Hearts 9", "Hearts 10", "Hearts Jack", "Hearts Quenn", "Hearts King",
       "Spades Ace", "Spades 2", "Spades 3", "Spades 4", "Spades 5", "Spades 6", "Spades 7", "Spades 8", "Spades 9", "Spades 10", "Spades Jack", "Spades Quenn", "Spades King"]
print("Всего карт в колоде: ",len(deck))
#Перемешиваем колоду.
random.shuffle(deck)

#Возвращаем случайный элемент списка, который будет козырем.
random_deck = random.choice(deck)

#Определяем индекс козыря.
trump = deck.index(random_deck)

#Удаляем по индексу элемент для переноса в конец списка.
deck.pop(trump)

#Добавляем в конец списка из Trump вырезанный элемент.
deck.append(random_deck)

#Выводим козырь.
print("Козырь объявлен: ",random_deck)
#First distribution
hand = deck[0:6]
for elem in hand:
        print(elem, end= '.')
deck = deck [6:]
while deck:
    #Запрос на сброс карт
    g = input("\n\nВыберите номера карт от 1 до 6 через , для сброса: ")
    #Проверка на ввод букв
    if g.isalpha():
        print("введена буква")
        continue
    #Проверка на пустую строку
    if not g:
        print("ты ничего не ввел")
        continue
    #Переделываем строку в список
    s = g.split(',')
    #Проверка на ввод цифр
    s1 = []
    for x in s:
        if x.isdigit():
            s1.append(int(x)-1)
    #Сортировка и удаление карт
    try:
        for n in sorted(s1, reverse=True):
            hand.pop(n)
    except IndexError:
        print("Вы ввели число больше 6")
        continue
    count_card = s1


def repeat(deck,hand,count_card):
    new_hand = hand + deck[:count_card]
    new_deck = deck[count_card:]
    return new_deck, new_hand

deck = repeat(deck)
hand = repeat(hand)