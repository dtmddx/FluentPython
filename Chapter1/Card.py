# Chapter 1

"""
One of the best qualities of Python is its consistency. After working with Python for a while, you are able to start
making informed, correct guesses about features that are new to you
"""

import collections

Card = collections.namedtuple("Card", ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JDKA")
    print("ranks: ", ranks)
    suits = "spades diamonds clubs hearts".split()
    print("suits: ", suits)

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


'''The first thing to note is the use of collections.namedtuple to construct a simple class to represent individual 
cards. Since Python2.6, namedtuple can be used to build classes of objects that are just bundles of attributes with 
no custom method, like a database record. In this example, we use it to provide a nice representation for the cards 
in the deck, as shown as in the console session: '''

beer_card = Card("7", "diamonds")

print("beer_card length: ", beer_card.__len__())
print(beer_card)



coordinate = collections.namedtuple("Coo", ["x", "y", "z"])
c1 = coordinate(1, 2, 3)
print("c1:", c1)

print("c1.x:", c1.x)
print("c1[0]: ", c1[0])

c2 = coordinate._make([100, 200, 300])
print("c2: ", c2)
print("c2.x: ", c2.x)

c2 = c2._replace(x = 300)
print("c2: ", c2)


deck = FrenchDeck()

