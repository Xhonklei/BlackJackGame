'''
This is Dealer class which has dealer main attributes and methods!
'''

class Dealer:
    def __init__(self):
        self.dealer_cards = []

    #new_card is the card drew from the main deck
    def draw_card(self,new_card):
        self.dealer_cards.append(new_card)     

    # To return all cards back to the deck
    def return_cards(self):
        played_cards = self.dealer_cards.copy()
        self.dealer_cards = []
        return played_cards
    
    def hand_score(self):
        score = 0
        ace_cards = []
        for card in self.dealer_cards:
            if card.rank == 'Ace':
                ace_cards.append(card)
            else:
                score += card.value
        for card in ace_cards:
            if 17<=(score + 10)<=21:
                score += 10
            else:
                score +=1
        return score

    def print_cards(self):
        #To have a view of dealer cards
        print(f'Dealer has the following cards:')
        for card in self.dealer_cards:
            print(card)
        print('\n')