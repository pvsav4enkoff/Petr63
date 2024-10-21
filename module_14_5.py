from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, update
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from crud_functions import *


api =  "7874058890:AAG5ytMjLAppzNZG2rSGtlci-sIPUYJbDx0"
bot=Bot(token=api)
dp=Dispatcher(bot, storage=MemoryStorage())

kb =ReplyKeyboardMarkup(resize_keyboard=True)
b1=KeyboardButton(text = "Рассчитать")
b2=KeyboardButton(text = "Информация")
b3=KeyboardButton(text = "Купить")
b4=KeyboardButton(text = "Регистрация")
kb.add(b1, b2, b3, b4)

kb2 =InlineKeyboardMarkup(resize_keyboard=True)
button = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data='calories')
button2 = InlineKeyboardButton(text = 'Формулы расчёта', callback_data='formulas')

kb2.add(button)
kb2.add(button2)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text="Продукт 1",callback_data="product_buying"),
            InlineKeyboardButton(text="Продукт 2",callback_data="product_buying"),
            InlineKeyboardButton(text="Продукт 3",callback_data="product_buying"),
            InlineKeyboardButton(text="Продукт 4",callback_data="product_buying")
        ]
    ], resize_keyboard= True
)

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000
class State(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    sex = State()


@dp.message_handler(commands = ['start'])
async def start(message):

    await message.answer(f'Привет! Я бот помогающий твоему здоровью.',reply_markup = kb)

@dp.message_handler(text = 'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup = kb2)

@dp.callback_query_handler(text = 'formulas')
async def inf_formula(call):
    await call.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.message.answer('для женщин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) - 161')
    await call.answer()

@dp.message_handler(text = 'Купить')
async def get_buying_list(message):
    initiate_db()
    rows = get_all_products()
    for row in rows:
        with open(row[3],"rb") as img:
            await message.answer(f'Название: {row[0]} | Описание: {row[1]} | Цена: {row[2]}' )
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=catalog_kb)

@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
           await call.message.answer(f"Вы успешно приобрели продукт!")
           await call.answer()

@dp.message_handler(text = 'Регистрация')
async def sing_up(message):
    initiate_db()
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()

@dp.message_handler(state = RegistrationState.username)
async def set_username(message, state):
    await state.update_data(username=message.text)
    if is_included(message.text):
        await message.answer("Пользователь существует, введите другое имя" )
        return RegistrationState.username
    data = await state.get_data()
    if is_latin(data['username']) == False:
        await message.answer("Только латинский алфавит, введите другое имя" )
        return RegistrationState.username

    await message.answer('Введите свой email:')
    await RegistrationState.email.set()

@dp.message_handler(state = RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()

@dp.message_handler(state = RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    try:
        # cursor = connection.cursor()
        if int(data['age']) <=0 or int(data['age'])>100:
            await message.answer(f"Не корректный возраст.\n Введите возраст")
            return RegistrationState.age
    except ValueError:
        await message.answer('Должна быть цифра.\n Введите возраст:')
        return RegistrationState.age
    await state.update_data(balance=RegistrationState.balance)
    await message.answer("Регистрация прошла успешно.")
    data = await state.get_data()
    add_user(data['username'],data['email'],data['age'],data['balance'])
    await state.finish()
@dp.callback_query_handler(text = 'calories')
async def set_age(call):
    await call.answer()
    await call.message.answer('Введите свой возраст:')
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
            await message.answer(f'Не верное значение возраст {data["age"]} (1-100).\n Введите возраст:')
            return State.age
            # await state.finish()
    except ValueError:
        await message.answer('Должна быть цифра.\n Введите возраст:')
        return State.age
@dp.message_handler(state = State.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    data = await state.get_data()
    try:
        if int(data['growth']) in range(50,250):
            await message.answer('Введите свой вес:')
            await State.weight.set()
        else:
            await message.answer(f'Не верное значение рост {data["growth"]} (50 - 250).\n Введите рост:')
            return State.growth
    except ValueError:
        await message.answer('Должна быть цифра.\n Введите рост:')
        return State.growth
@dp.message_handler(state = State.weight)
async def set_weight(message, state):
    await state.update_data(weigth=message.text)
    data = await state.get_data()
    try:
        if int(data['weigth']) in range(30,200):
            await message.answer('Введите свой пол (1 - муж, 2 - жен):')
            await State.sex.set()
        else:
            await message.answer(f'Не верное значение вес {data["weigth"]} (30 -200).\n Введите вес:')
            return State.weight
    except ValueError:
        await message.answer('Должна быть цифра.\n Введите вес:')
        return State.weight
@dp.message_handler(state = State.sex)
async def send_calories(message, state):
    await state.update_data(sex=message.text)
    data = await state.get_data()
    # для     мужчин: 10     х     вес(кг) + 6, 25    x    рост(см) – 5    х    возраст(г) + 5;
    # для     женщин: 10     х     вес(кг) + 6, 25    x    рост(см) – 5    х    возраст(г) - 161;
    try:
        if int(data['sex']) == 1:
            Calories= (10*int(data['weigth']))+(6.25 * int(data['growth']))-(5*int(data['age']))+5
        elif int(data['sex']) == 2:
            Calories = (10 * int(data['weigth'])) + (6.25 * int(data['growth'])) - (5 * int(data['age']))-161
        else:
            await message.answer(f"Не верное значение пол {data['sex']} (1 - муж, 2 - жен).\n Введите пол:")
            return State.sex
    except ValueError:
        await message.answer('Должна быть цифра.\n Введите пол:')
        return State.sex
    await message.answer(f"Ваша норма калорий {Calories} ккал")
    await state.finish()




if __name__ == "__main__":
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()
    executor.start_polling(dp, skip_updates=True)
    connection.commit()
    connection.close()
