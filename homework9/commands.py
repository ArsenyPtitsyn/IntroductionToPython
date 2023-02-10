from random import randint
from aiogram import types
import model, view


async def start_game(message: types.Message):
    await model.set_game()
    await view.game_rules(message)
    name = message.from_user.first_name
    await model.set_player_name(name)
    first_turn = randint(0, 1)
    if first_turn == 1:
        await view.player_move(message)
    else:
        await bot_turn(message)

async def bot_turn(message):
    take = await model.bot_take()
    await model.set_number_of_sweets(take)
    name = await model.get_player_name()
    number_of_sweets = await model.get_number_of_sweets()
    if await model.get_number_of_sweets() > 0:
        await view.table_info(message, 'Бот', take, number_of_sweets, name)
    if await model.get_number_of_sweets() <= 0:
        await view.win(message, 'Бот', take, number_of_sweets)
        await model.set_game()

async def player_turn(message):
    game = await model.get_game()
    if game:
        if message.text == '/start':
            return
        else:
            take = int(message.text)
            if take > 0 and take <= 28:
                await model.set_number_of_sweets(take)
            else:
                await view.wrong_take(message)
        name = await model.get_player_name()
        number_of_sweets = await model.get_number_of_sweets()
        if await model.get_number_of_sweets() > 0:
            await view.table_info(message, name, take, number_of_sweets, 'Бот')
            await bot_turn(message)
        if await model.get_number_of_sweets() <= 0:
            await view.win(message, name, take, number_of_sweets)
            await model.set_game()