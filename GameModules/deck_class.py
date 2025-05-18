'''
This is the Deck class with 2 options
Shuffle-> to shuffle the cards and
deal -> to deal out the cards depending on the number of players.
'''
import random
#Importing Card class, suits and ranks
#  to form the deck of the game
from GameModules.card_class import Card, suits, ranks

class Deck:

    def __init__(self):
        # Create the deck with all cards combinations
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
    
    # This is the length function of the Deck 
    def __len__(self):
        return len(self.all_cards)
    
    # This does the shuffling of all the deck
    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    # This is the string function of the deck, to check it.
    def __str__(self):
        for card in self.all_cards:
            print(card)
        return 'This is the deck you have!'
    
    # This is the function that remove one card 
    # from top of the deck
    def deal_one(self):
        return self.all_cards.pop()
    
    # This is the function that adds back 
    # all the played card into the deck.
    def add_cards(self, played_cards):
        self.all_cards = played_cards + self.all_cards