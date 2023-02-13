from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram import types
import model, view

AVAILABLE_OPERATIONS = ['+', '-', '*', '/']

class CalcStates(StatesGroup):
    waiting_for_first_number = State()
    waiting_for_operation = State()
    waiting_for_second_number = State()

async def send_welcome(message: types.Message, state: FSMContext):
    await state.finish()
    await view.velcome_message(message)


async def calculate(message: types.Message):
    await view.enter_first_number(message)
    await CalcStates.waiting_for_first_number.set()

async def choosing_first_number(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await view.incorrect_input(message)
        return
    await state.update_data(first_number=int(message.text))
    await CalcStates.next()
    await view.enter_operation(message)


async def choosing_operation(message: types.Message, state: FSMContext):
    if message.text not in VAILABLE_OPERATIONS:
        await view.incorrect_input(message)
        return
    await state.update_data(operation=message.text)
    await CalcStates.next()
    await view.enter_second_number(message)


async def choosing_second_number(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await view.incorrect_input(message)
        return
    user_data = await state.get_data()
    oper = user_data['operation']
    first_number = user_data['first_number']
    second_number = int(message.text)
    result = 0
    if oper == '+':
        result = first_number + second_number
    elif oper == '-':
        result = first_number - second_number
    elif oper == '*':
        result = first_number * second_number
    elif oper == '/':
        result = first_number / second_number
    await message.answer(f'Результат {result}')
    await state.finish()
