def player_situation(pl, deck, played_cards):
    '''
    des: Calculate the score of the player and based on this action are taken
         ---> Hit or stay
         ---> Socre 21
         ---> Busted
    
    args: player on focus, deck of the game, list of played cards
    
    return: p_out(Boolean if player still on game or not)
            played_cards (list of played cards so far!) 
    
    
    '''
    p_out = False
    possible_choice =('h','H','s','S')
    player_stays = False
    p_score = pl.hand_score()
    # If player's hand score is lower than 21 ask him if he wants to hit or stay!
    while(p_score < 21 ):
        while True:
            decision = str(input(f'{pl.name} do you want to Hit or Stay? (H -> HIT|S ->STAY): '))
            if decision not in possible_choice:
                print(f'Please choose one of the {possible_choice}!')
                continue
            # If hit, draw a card and recalcualte hand score.
            elif decision == 'h' or decision =='H':
                pl.draw_card(deck.deal_one())
                print(f'{pl.name} drew {pl.player_cards[-1]}.')
                p_score = pl.hand_score()
                break
            # If stay do nothing.
            elif decision == 's' or decision =='S':
                print(f'{pl.name} stays with his actual hand.')
                player_stays = True
                break
        if player_stays == True:
            break
    # If player's hand score equal to 21: Update his balance, 
    # reset bet, get played cards, and remove him from the actual round.
    if p_score == 21:
        print(f'{pl.name} scored 21, and profitted {int(pl.bet * 1.5)}$ this round!')
        pl.balance += int(pl.bet * 2.5)
        pl.bet = 0
        played_cards += pl.return_cards()
        p_out = True
    # If busted, reset bet, get played cards, and remove from actual round.
    elif p_score > 21:
        print(f'{pl.name} busted, and lost {int(pl.bet)}$ this round!')
        pl.bet = 0
        played_cards += pl.return_cards()
        p_out = True
    
    return p_out, played_cards
    

     