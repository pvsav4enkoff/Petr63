from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, update
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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
