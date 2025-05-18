'''
This is player class which has players main attributes and methods!
'''

class Player:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.player_cards = []
        self.bet = 0

    def __str__(self):
        return 'This is ' + self.name + ' and has a balance of ' + str(self.balance) +'$.'

    #new_card is the card drew from the main deck
    def draw_card(self,new_card):
        self.player_cards.append(new_card)

    def return_cards(self):
        played_cards = self.player_cards.copy()
        self.player_cards = []
        return played_cards


    
    # To set a bet for the round:
    def set_bet(self):
        while True:
            try:
                placed_bet = int(input(f'{self.name}, please enter your bet between 1$ and {self.balance}$ for this round: '))
            except ValueError:
                print('Please, set a integer value!')
            else:
                if self.balance == 0:
                    print('You cannot set a bet!')
                    break
                elif placed_bet <= 0 or placed_bet > self.balance:
                    print("OUT OF BALANCE !")
                    continue
                else:
                    self.bet = placed_bet
                    self.balance -=self.bet
                    print(f'{self.name} just placed a bet of {self.bet}$!\nLeft balance: {self.balance}$...')
                    break
    # To get the total score of cards on the hand
    def hand_score(self):
        score = 0
        for card in self.player_cards:
            if card.rank == 'Ace':
                while True:
                    try:
                        ace_score = int(input(f'{self.name}, choose the value of Ace, 1 or 10: '))
                    except ValueError:
                        print("Please enter integer!")
                        continue
                    else:
                        if ace_score != 1 and ace_score != 10:
                            print("Please choose 1 or 10!")
                            continue
                        else:
                            score +=ace_score
                            break
            else:
                score += card.value
        return score
    
    def print_cards(self):
        #To have a view of player deck
        print(f'\n{self.name} has the following cards:')
        for card in self.player_cards:
            print(card)