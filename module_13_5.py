from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import asyncio

api =  ""
bot=Bot(token=api)
dp=Dispatcher(bot, storage=MemoryStorage())

kb =ReplyKeyboardMarkup(resize_keyboard=True)
b1=KeyboardButton(text = "Расчитать")
b2=KeyboardButton(text = "Информация")
kb.add(b1)
kb.add(b2)
class State(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    sex = State()
@dp.message_handler(commands = ['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.',reply_markup = kb)


@dp.message_handler(text = 'Расчитать')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await State.age.set()
@dp.message_handler(state = State.age)
async def set_growth(message,state):
    await state.update_data(age=message.text)
    data = await state.get_data()

    try:
        if int(data['age']) in range(1,100):
            await message.answer('Введите свой рост:')
            await State.growth.set()
        else:
            await message.answer('Не верное значение возраст (1-100). Тест прерван')
            await state.finish()
    except ValueError:
        await message.answer('Должна быть цифра. Тест прерван')
        await state.finish()
@dp.message_handler(state = State.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    data = await state.get_data()
    try:
        if int(data['growth']) in range(50,250):
            await message.answer('Введите свой вес:')
            await State.weight.set()
        else:
            await message.answer('Не верное значение рост (50 - 250). Тест прерван')
            await state.finish()
    except ValueError:
        await message.answer('Должна быть цифра. Тест прерван')
        await state.finish()
@dp.message_handler(state = State.weight)
async def set_weight(message, state):
    await state.update_data(weigth=message.text)
    data = await state.get_data()
    try:
        if int(data['weigth']) in range(30,200):
            await message.answer('Введите свой пол (1 - муж, 2 - жен):')
            await State.sex.set()
        else:
            await message.answer('Не верное значение вес (30 -200). Тест прерван')
            await state.finish()
    except ValueError:
        await message.answer('Должна быть цифра. Тест прерван')
        await state.finish()
@dp.message_handler(state = State.sex)
async def send_calories(message, state):
    await state.update_data(sex=message.text)
    data = await state.get_data()
    # для     мужчин: 10     х     вес(кг) + 6, 25    x    рост(см) – 5    х    возраст(г) + 5;
    # для     женщин: 10     х     вес(кг) + 6, 25    x    рост(см) – 5    х    возраст(г) - 161;
    # if data['sex'].isdigit():
    try:
        if int(data['sex']) == 1:
            Calories= (10*int(data['weigth']))+(6.25 * int(data['growth']))-(5*int(data['age']))+5
        elif int(data['sex']) == 2:
            Calories = (10 * int(data['weigth'])) + (6.25 * int(data['growth'])) - (5 * int(data['age']))-161
        else:
            await message.answer(f"Не верное значение пол (1 - муж, 2 - жен). Тест прерван")
    except ValueError:
        await message.answer('Должна быть цифра. Тест прерван')
        await state.finish()
    await message.answer(f"Ваша норма калорий {Calories}")
    await state.finish()




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
