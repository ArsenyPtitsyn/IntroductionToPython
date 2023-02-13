from aiogram import types

async def write_first_number(message: types.Message):
    await message.answer('Напишите первое число: ')

async def velcome_message(message: types.Message):
    await message.answer("Привет!\nЯ - бот-калькулятор\nВведите команду /calc для начала вычислений")