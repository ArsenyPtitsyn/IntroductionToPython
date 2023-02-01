from random import randint
#5634428782:AAFbmMYfbXL8zqprhFql5VKzMbwKizJ2vNU
candies = 221
player1 = None
player2 = None
game_mode = 1


def choose_game_mode():
    global game_mode
    game_mode = int(input('If you want to play with human enter "1", with computer - "2".'))
    return game_mode


def pvp_representation():
    global player1, player2
    player1 = input('First player enter your name: ')
    player2 = input('Second player enter your name: ')


def pvm_representation():
    global player1, player2
    player1 = input('Enter your name: ')
    player2 = 'Computer'
    print(f'Opponents: {player1} and {player2}')


def human_turn(player):
    global candies
    while True:
        print(f'Now on the table {candies} candies!')
        n = int(input(f'{player}! Enter number of candies (from 1 to 28): '))
        if n > 28 or n < 1:
            print('Impossible!')
        else:
            candies -= n
            if candies < 0:
                print(f"You can''t take more then {candies} candies!")
                candies += n
                continue
            break


def ai_turn():
    global candies
    taken_candies = candies % 29
    if taken_candies != 0:
        candies -= taken_candies
    else:
        taken_candies = randint(1, 28)
        candies -= taken_candies
    print(f'Computer takes {taken_candies} candies and now on the table {candies} candies!')


def check_win(player):
    global candies
    return candies == 0


def toss():
    if randint(1, 10) > 5:
        return player1
    else:
        return player2


def change_player(player):
    global player1, player2
    if player == player1:
        return player2
    if player == player2:
        return player1



game_mode = choose_game_mode()
if game_mode == 1:
    pvp_representation()
    player = toss()
    while True:
        human_turn(player)
        if check_win(player):
            print(f'{player} win!')
            break
        player = change_player(player)
elif game_mode == 2:
    pvm_representation()
    player = toss()
    while True:
        if player == 'Computer':
            ai_turn()
            if check_win(player):
                print(f'{player} win!')
                break
            player = change_player(player)
        else:
            human_turn(player)
            if check_win(player):
                print(f'{player} win!')
                break
            player = change_player(player)
else:
    print('Not described game mode!')
