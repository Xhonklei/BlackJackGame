"""
Created on Sun May 18 20:10:25 2025

@author: Xhonklei
"""

from GameModules.deck_class import Deck
from GameModules.player_class import Player
from GameModules.dealer_class import Dealer
from GameModules.initiatePlayers import initiate_players
from GameModules.playerSituation import player_situation
from GameModules.dealerOn import dealer_on
from GameModules.ContinueDecision import continue_decision
import time 
import os


def black_jack_game():

    # Create the deck, dealer and players of the game.
    deck_of_game = Deck()
    deck_of_game.shuffle_deck()
    game_dealer = Dealer()
    players = initiate_players()

    # For as long as there are players on the game
    while len(players) !=0:
        i = 0
        j = 0
        played_cards = []
        # Each player palces his bet
        while i < len(players):
            players[i].set_bet()
            i += 1

        #Draw 2 cards for each player and for the dealer
        for j in range(2):
            for player in players:
                player.draw_card(deck_of_game.deal_one())
            game_dealer.draw_card(deck_of_game.deal_one())
    
        # print('After each player and dealer got 2 cards, the situation is:\n')
        # for player in players:
        #     player.print_cards()
        print(f'\nFirst card of the dealer is:\n{game_dealer.dealer_cards[0]}')

        # See who profits this round:
        round_players = players.copy() # Players of the actual round
        i = 0
        while i < len(round_players):
            round_players[i].print_cards()
            player_out = False
            player_out, played_cards = player_situation(round_players[i],deck_of_game,played_cards)
            if player_out == True:
                round_players.pop(i)
            else:
                i += 1
    
        # If there are still players left on the round, dealer enters the game.
        if len(round_players) != 0:
            print('\n')
            game_dealer.print_cards()
            # The whole logic of the dealer entering the game is implemented here!
            played_cards = dealer_on(game_dealer, round_players, deck_of_game, played_cards)
    
        #Return played cards back in the deck and shuffle it.
        played_cards += game_dealer.return_cards()
        deck_of_game.add_cards(played_cards)
        deck_of_game.shuffle_deck()

        # Ask players if they want to play or not.
        players = continue_decision(players)

        print('\nA new round is about to start...')
        time.sleep(5)
        os.system('clear')
    
    print('There is no player on the table!')
    print('GAME OVER!')

if __name__ =='__main__':
    black_jack_game()
