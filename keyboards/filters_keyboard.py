from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
print('filters_keyboard')

inv_b=KeyboardButton('/inversion')
sobel_b=KeyboardButton('/sobel')
grey_b=KeyboardButton('/grey_scale')
glass_b=KeyboardButton('/glass')
menu_b=KeyboardButton('/main_menu')

filters_kd=ReplyKeyboardMarkup(resize_keyboard=True)

filters_kd.row(inv_b,sobel_b).row(grey_b,glass_b).add(menu_b)