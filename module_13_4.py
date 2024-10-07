from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api =  ""
bot=Bot(token=api)
dp=Dispatcher(bot, storage=MemoryStorage())
class State(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    sex = State()

@dp.message_handler(text = 'Calories')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await State.age.set()

@dp.message_handler(state = State.age)
async def set_growth(message,state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await State.growth.set()

@dp.message_handler(state = State.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await State.weight.set()

@dp.message_handler(state = State.weight)
async def set_weight(message, state):
    await state.update_data(weigth=message.text)
    await message.answer('Введите свой пол (1 - муж, 2 - жен):')
    await State.sex.set()

@dp.message_handler(state = State.sex)
async def send_calories(message, state):
    await state.update_data(sex=message.text)
    data = await state.get_data()
    # для     мужчин: 10     х     вес(кг) + 6, 25    x    рост(см) – 5    х    возраст(г) + 5;
    # для     женщин: 10     х     вес(кг) + 6, 25    x    рост(см) – 5    х    возраст(г) - 161;
    # Calories=0
    if int(data['sex']) == 1:
        Calories= (10*int(data['weigth']))+(6.25 * int(data['growth']))-(5*int(data['age']))+5
        await message.answer(f"Ваша норма калорий {Calories}")
    elif int(data['sex']) == 2:
        Calories = (10 * int(data['weigth'])) + (6.25 * int(data['growth'])) - (5 * int(data['age']))-161
        await message.answer(f"Ваша норма калорий {Calories}")
    else:
        await message.answer(f"Не верное значение пол (1 - муж, 2 - жен)")

    await state.finish()




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
