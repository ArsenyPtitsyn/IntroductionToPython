from bot import bot

async def show_commands_info(message):
    await bot.send_message(message.from_user.id, f'С помощью данного калькулятора вы можете совершать различные арифметические \n'
                                                 f'действия с вещественными числами:\nскладывать - /sum\nвычитать - /dif\n умножать - /mul\n'
                                                 f'делить - /div')

