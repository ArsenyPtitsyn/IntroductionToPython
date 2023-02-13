from aiogram import types

async def velcome_message(message: types.Message):
    await message.answer("Привет!\nЯ - бот-калькулятор\nВведите команду /calc для начала вычислений")

async def enter_first_number(message: types.Message):
    await message.answer('Напишите первое число: ')

async def incorrect_input(message: types.Message):
    await message.answer('Некоректный ввод. Попробуйте снова.')

async def enter_operation(message: types.Message):
    await message.answer('Теперь введите операцию: ')

async def enter_second_number(message: types.Message):
    await message.answer('Введите второе число: ')

