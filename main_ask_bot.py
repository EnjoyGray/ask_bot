from database.qst_database import qst_inv200, qst500
from aiogram import Bot, Dispatcher, executor, types
from markups import markups
from markups.token import MyApiTOKEN


API_TOKEN = MyApiTOKEN
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def commad_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Бот підключенний!👋', reply_markup=markups.mainMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == '❕Я ніколи не...❕':
        await bot.send_message(message.from_user.id, f'{qst_inv200()}', reply_markup=markups.mainMenu)

    elif message.text == '❗️Рандомне питання❗️':
        await bot.send_message(message.chat.id, f"{qst500()}.❓", reply_markup=markups.mainMenu)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
