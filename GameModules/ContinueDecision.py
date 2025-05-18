def continue_decision(players_on_table):
    '''
    des: Asks each player if they want to continue play or not.

    args: Existing players on table
    
    return: Left players on table
    '''  
    possible_choices =('y','Y','n','N')
    i = 0
    while i < len(players_on_table):
        # First check if player has enough balance to play.
        if players_on_table[i].balance == 0:
            print(f'{players_on_table[i].name} is out of the table!')
            players_on_table.pop(i)
        else:
            while True:
                try:
                    answer = str(input(f'{players_on_table[i].name}, do you want to play? (y -> YES | n -> NO): '))
                except answer not in possible_choices:
                    print(f'Please choose between {possible_choices}!')
                    continue
                else:
                    if answer in ('n','N'):
                        print(f'{players_on_table[i].name} left the game!')
                        players_on_table.pop(i)
                        break
                    elif answer in ('y','Y'):
                        i +=1
                        break

    return players_on_table