from aiogram import Dispatcher
import commands

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(
        commands.start_calculation, commands='calc'
    )
    dp.register_message_handler(
        commands.choosing_first_number, state=commands.CalcStates.waiting_for_first_number
    )
    dp.register_message_handler(
        commands.choosing_operation, state=commands.CalcStates.waiting_for_operation
    )
    dp.register_message_handler(
        commands.choosing_second_number, state=commands.CalcStates.waiting_for_second_number
    )
    dp.register_message_handler(
        commands.send_welcome, commands='start'
    )