def dealer_on(game_dealer, game_players, deck, played_cards):
    '''
    des: This is the logic of game when dealer enters the game.
         Rules of BlackJack are followed!

    args: dealer of the game, players competing with dealer,
          deck of the game, and played cards so far.
    
    return: played_cards (list of cards played that round)
    '''

    # First, dealer has to draw cards until his hand socres more than 17.
    while (game_dealer.hand_score() < 17):
        game_dealer.dealer_cards.append(deck.deal_one())
        print(f'Dealer drew {game_dealer.dealer_cards[-1]}.')
        
    #If dealer busted update players balance and reset bet.
    if game_dealer.hand_score() > 21:
        print('Dealer busted! All remaining players wins.')
        for player in game_players:
            player.balance += int(player.bet * 2)
            player.bet = 0
            played_cards += player.return_cards()
    # If not, then for each player check if they profit or lose, based on the game's rules. 
    else:
        for pl in game_players:
            p_score = pl.hand_score()
            if p_score > game_dealer.hand_score():
                print(f'{pl.name} won his bet, and profitted {int(pl.bet * 1)}$ this round!')
                pl.balance += int(pl.bet * 2)
                pl.bet = 0
            elif p_score == game_dealer.hand_score():
                print(f'{pl.name} did not profit anything this round!')
                pl.balance += pl.bet
                pl.bet = 0
            else:
                print(f'{pl.name} lost his bet of {int(pl.bet)}$ this round!')
                pl.bet = 0
            played_cards += pl.return_cards()
    
    return played_cards