from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
print('filters_keyboard')

load_im_b=KeyboardButton('/load_image')
inv_b=KeyboardButton('/inversion')
sobel_b=KeyboardButton('/sobel')
grey_b=KeyboardButton('/grey_scale')
glass_b=KeyboardButton('/glass')
menu_b=KeyboardButton('/main_menu')

filters_kd=ReplyKeyboardMarkup(resize_keyboard=True)

filters_kd.add(load_im_b).row(inv_b,sobel_b).row(grey_b,glass_b).add(menu_b)