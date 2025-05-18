# This is the function to create all the players of the game
from GameModules.player_class import Player

def initiate_players():
    '''
    des: Asks for number of players, their names and their amounts. 
         Based on the inputs, players are initiated based on Player class. 

    args = None
    return = players of the game

    '''
    while True:
        try:
            num_player = int(input('How many player are going to play?: '))
        except ValueError:
            print('Please, enter an integer!')
            continue
        else:
            break

    players =[]
    for i in range(num_player):
        player_name = input(f'Enter name of {i+1} player: ')
        while True:
            try:
                player_balance = int(input(f'Enter balance of {player_name}:'))
            except ValueError:
                print('It is asking for balance. Please enter an amount as integer!')
                continue
            else:
                break
        players.append(Player(player_name,player_balance))
    
    return players

