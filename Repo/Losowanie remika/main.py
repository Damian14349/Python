# losowanie do remika

import random

deck = ["As pik", "As kier", "As kar", "As trefl",
        "Król pik", "Król kier", "Król kar", "Król trefl",
        "Dama pik", "Dama kier", "Dama kar", "Dama trefl",
        "Walet pik", "Walet kier", "Walet kar", "Walet trefl",
        "10 pik", "10 kier", "10 kar", "10 trefl",
        "9 pik", "9 kier", "9 kar", "9 trefl",
        "8 pik", "8 kier", "8 kar", "8 trefl",
        "7 pik", "7 kier", "7 kar", "7 trefl",
        "6 pik", "6 kier", "6 kar", "6 trefl",
        "5 pik", "5 kier", "5 kar", "5 trefl",
        "4 pik", "4 kier", "4 kar", "4 trefl",
        "3 pik", "3 kier", "3 kar", "3 trefl",
        "2 pik", "2 kier", "2 kar", "2 trefl",
        ]

def shuffle():
        random.shuffle(deck)

def deal():
        player1 = []
        player2 = []
        player3 = []
        player4 = []
        for i in range(5):
                player1.append(deck.pop())
                player2.append(deck.pop())
                player3.append(deck.pop())
                player4.append(deck.pop())
                i += 1

        #zagnieżdżona funkcja wyświetlająca
        def show():
                print(player1)
                print(player2)
                print(player3)
                print(player4)
        show()

shuffle()
deal()