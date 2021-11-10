from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove
print('main_keyboard')
help_b=KeyboardButton('/help')
info_b=KeyboardButton('/info')
process_b=KeyboardButton('/process')

main_kd=ReplyKeyboardMarkup(resize_keyboard=True)

main_kd.add(process_b).row(help_b,info_b)