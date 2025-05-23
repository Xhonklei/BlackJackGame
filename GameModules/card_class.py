'''
This is a Card class
'''
# These are the default suits and ranks
#  from where we form all the cards of the deck
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
# values assign a value for each card, corresponding to BlackJack game rules.
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':1}

class Card:

    # Each card has its own suit, rank and value
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    # Str function to print each card
    def __str__(self):
        return self.rank + ' of ' + self.suit
    