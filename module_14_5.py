from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import handlers
from handlers import *

api =  ""
bot=Bot(token=api)
dp=Dispatcher(bot, storage=MemoryStorage())

dp.message_handler(commands = ['start'])(handlers.start)
dp.message_handler(text = 'Рассчитать')(handlers.main_menu)
dp.callback_query_handler(text = 'formulas')(handlers.inf_formula)
dp.message_handler(text = 'Купить')(handlers.get_buying_list)
dp.callback_query_handler(text="product_buying")(handlers.send_confirm_message)
dp.message_handler(text = 'Регистрация')(handlers.sing_up)
dp.message_handler(state = RegistrationState.username)(handlers.set_username)
dp.message_handler(state = RegistrationState.email)(handlers.set_email)
dp.message_handler(state = RegistrationState.age)(handlers.set_age_user)
dp.callback_query_handler(text = 'calories')(handlers.set_age)
dp.message_handler(state = State.age)(handlers.set_growth)
dp.message_handler(state = State.growth)(handlers.set_weight)
dp.message_handler(state = State.weight)(handlers.set_sex)
dp.message_handler(state = State.sex)(handlers.send_calories)

if __name__ == "__main__":
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()
    executor.start_polling(dp, skip_updates=True)
    connection.commit()
    connection.close()
