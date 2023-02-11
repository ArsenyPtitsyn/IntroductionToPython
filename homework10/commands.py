from aiogram import types
import model, view

async def start_calculator(message: types.Message):
    await view.show_commands_info(message)
