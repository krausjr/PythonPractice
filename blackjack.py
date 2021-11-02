import random

class Card:
    def __init__(self, value, suit):
        self.value = value 
        self.suit = suit 
    
    def show(self):
        print('{} of {}'.format(self.value, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ['hearts', 'diamonds', 'clubs', 'spades']:
            for v in ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']:
                self.cards.append(Card(v,s))
    
    def show(self):
        for c in self.cards:
            c.show()
               
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)
    
    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)

deck = Deck()
deck.shuffle()
deck.show()

# class Player:
#     def __init__(self, player, dealer):
#         self.player = player
#         self.dealer = dealer