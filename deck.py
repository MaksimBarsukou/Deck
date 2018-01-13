#Подключаем модуль рандома.
import random 
#Создаем список карт.
deck = ["Clubs Ace", "Clubs 2", "Clubs 3", "Clubs 4", "Clubs 5", "Clubs 6", "Clubs 7", "Clubs 8", "Clubs 9", "Clubs 10", "Clubs Jack", "Clubs Quenn", "Clubs King",
       "Diamonds Ace", "Diamonds 2", "Diamonds 3", "Diamonds 4", "Diamonds 5", "Diamonds 6", "Diamonds 7", "Diamonds 8", "Diamonds 9", "Diamonds 10", "Diamonds Jack", "Diamonds Quenn", "Diamonds King",
       "Hearts Ace", "Hearts 2", "Hearts 3", "Hearts 4", "Hearts 5", "Hearts 6", "Hearts 7", "Hearts 8", "Hearts 9", "Hearts 10", "Hearts Jack", "Hearts Quenn", "Hearts King",
       "Spades Ace", "Spades 2", "Spades 3", "Spades 4", "Spades 5", "Spades 6", "Spades 7", "Spades 8", "Spades 9", "Spades 10", "Spades Jack", "Spades Quenn", "Spades King"]
print(len(deck))
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
print("Козырь обьявлен: ",random_deck)

#Раздаем карты.
hand = deck[0:6]
print("Ваши карты:",hand)
#for elem in hand:
    #print(elem, end=' . ')
deck = deck[6:]
print(len(deck))
#Запрос на номера карт для сброса, значение хранит переменная x.
s = list(input("\n\nВыберите номера 3 карт для сброса: ").split(','))
#s = [int(x)-1 for x in s if x.isdigit()]
for x in s:
    s1 = []
    for x in s:
        if x.isdigit():
            s1.append(int(x)-1)
            



print(s1)