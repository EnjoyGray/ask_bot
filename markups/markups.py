from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# ---main menu---
i_nvn = KeyboardButton('❕Я ніколи не...❕', row_width=1)
qst_gen = KeyboardButton('❗️Випадкове питання❗️', row_width=1)

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(i_nvn, qst_gen)
