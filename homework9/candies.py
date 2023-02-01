from random import randint

candies = 221
player1 = None
player2 = None
game_mode = 1


def choose_game_mode():
    global game_mode
    game_mode = int(input('Если вы хотите играть с человеком, нажмите "1", если с компьютером - "2".'))
    return game_mode


def pvp_representation():
    global player1, player2
    player1 = input('Первый игрок, введите своё имя: ')
    player2 = input('Второй игрок, введите своё имя: ')


def pvm_representation():
    global player1, player2
    player1 = input('Введите своё имя: ')
    player2 = 'Компьютер'


def human_turn(player):
    global candies
    while True:
        print(f'Сейчас на столе {candies} конфет!')
        n = int(input(f'{player}! Введите количество конфект, которое вы хотите взять (от 1 до 28): '))
        if n > 28 or n < 1:
            print('Неверный ввод!')
        else:
            candies -= n
            if candies < 0:
                print('Вы не можете взять конфет больше, чем лежит на столе!')
                candies += n
                continue
            break


def ai_turn():
    global candies
    taken_candies = candies % 29
    candies -= taken_candies
    print(f'Компьютер взял {taken_candies} конфет и теперь на столе {candies} конфет!')


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
    else:
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
        if player == 'AI':
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

