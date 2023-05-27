from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# ---main menu---
i_nvn = KeyboardButton('❕Я ніколи не...❕')
qst_gen = KeyboardButton('❗️Випадкове питання❗️')
couple = KeyboardButton('👫Для двох👫')


mainMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(i_nvn, qst_gen, couple)
