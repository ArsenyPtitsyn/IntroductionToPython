from bot import bot


async def game_rules(message):
    await bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}\n'
                                                 f'Правила: На столе лежит 221 конфета. Играет два игрока делая ход'
                                                 f'друг после друга. Первый ход определяется жеребьёвкой. За один ход'
                                                 f'можно забрать не более 28 конфет. Побеждает тот, кто забрал '
                                                 f'последнюю конфету')

async def player_move(message):
    await bot.send_message(message.from_user.id, f'Возьмите конфеты, но не более 28!')

async def table_info(message, name1, take, number_of_sweets, name2):
    await bot.send_message(message.from_user.id, f'{name1} взял {take} конфет, \n'
                                                 f'на столе осталось {number_of_sweets} конфет.'
                                                 f'Ход {name2}.')

async def win(message, name, take, number_of_sweets):
    await bot.send_message(message.from_user.id, f'{name} взял {take} конфет,\n'
                                                 f'на столе осталось {number_of_sweets} конфет.\n'
                                                 f'{name} победил!')

async def wrong_take(message):
    await bot.send_message(message.from_user.id, f'Вы взяли недопустимое количество конфет!\n'
                                                 f'Попробуйте ещё раз!\n'
                                                 f'Конфет должно быть больше 0 и не больше чем 28!')

