import random


class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def show(self):
        print(f'{self.val} of {self.suit}')


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for s in ['Heart', 'Diamond', 'Spade', 'Club']:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()
    
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()


deck = Deck()
deck.shuffle()

print("Ganesh")
Ganesh = Player('Ganesh')
Ganesh.draw(deck).draw(deck).draw(deck)
Ganesh.showHand()
print()

print("Tapen")
tapen = Player('Tapen')
tapen.draw(deck).draw(deck).draw(deck)
tapen.showHand()