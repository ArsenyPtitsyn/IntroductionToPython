from random import randint

candies = 221
player1 = None
player2 = None


def players_representation():
    global player1, player2
    player1 = input('Первый игрок, введите своё имя: ')
    player2 = input('Второй игрок, введите своё имя: ')


def turn(player):
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


players_representation()
player = toss()
while True:
    turn(player)
    if check_win(player):
        print(f'{player} win!')
        break
    player = change_player(player)
