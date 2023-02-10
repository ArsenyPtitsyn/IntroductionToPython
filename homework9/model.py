from random import randint


game = False
player_name = ''
number_of_sweets = 221

async def  set_game():
    global game
    global player_name
    global number_of_sweets
    if game == False:
        game = True
    else:
        player_name = ''
        number_of_sweets = 221
        game = False

async def set_player_name(name):
    global player_name
    player_name = name

async def bot_take():
    global number_of_sweets
    take_sweets = number_of_sweets % 29 if number_of_sweets % 29 != 0 else randint(1, 28)
    return take_sweets

async def set_number_of_sweets(take):
    global number_of_sweets
    number_of_sweets -= take

async def get_player_name():
    global player_name
    return player_name

async def get_number_of_sweets():
    global number_of_sweets
    return number_of_sweets

async def get_game():
    global game
    return game