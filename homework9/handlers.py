from aiogram import Dispatcher
import commands

def registered_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start_game, commands=['start'])
    dp.register_message_handler(commands.player_turn)