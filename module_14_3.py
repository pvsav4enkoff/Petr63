from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, update
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from telegram.ext import Updater, CommandHandler, MessageHandler

api =  ""
bot=Bot(token=api)
dp=Dispatcher(bot, storage=MemoryStorage())



kb =ReplyKeyboardMarkup(resize_keyboard=True)
b1=KeyboardButton(text = "Рассчитать")
b2=KeyboardButton(text = "Информация")
b3=KeyboardButton(text = "Купить")
kb.add(b1, b2, b3)
#
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
    with open('image_1.jpg',"rb") as img1:
        await message.answer('Название: Product1 | Описание: описание 1 | Цена: 100' )
        await message.answer_photo(img1)
    with open('image_2.jpg', "rb") as img2:
        await message.answer('Название: Product2 | Описание: описание 2 | Цена: 200')
        await message.answer_photo(img2)
    with open('image_3.jpg', "rb") as img3:
        await message.answer('Название: Product3 | Описание: описание 3 | Цена: 300')
        await message.answer_photo(img3)
    with open('image_4.jpg', "rb") as img4:
        await message.answer('Название: Product4 | Описание: описание 4 | Цена: 400')
        await message.answer_photo(img4)

    await message.answer('Выберите продукт для покупки:', reply_markup=catalog_kb)

@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
           await call.message.answer(f"Вы успешно приобрели продукт!")
           await call.answer()

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
            await message.answer(f'Не верное значение возраст {data["age"]} (1-100). Тест прерван')
            # await state.finish()
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
            await message.answer(f'Не верное значение рост {data["growth"]} (50 - 250). Тест прерван')
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
            await message.answer(f'Не верное значение вес {data["gweigth"]} (30 -200). Тест прерван')
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
            await message.answer(f"Не верное значение пол {data['sex']} (1 - муж, 2 - жен). Тест прерван")
    except ValueError:
        await message.answer('Должна быть цифра. Тест прерван')
        await state.finish()
    await message.answer(f"Ваша норма калорий {Calories} ккал")
    await state.finish()




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
