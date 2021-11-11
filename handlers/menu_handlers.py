
from os import stat
from aiogram import types,Dispatcher
from create_bot import dp,bot
from keyboards import main_kd,filters_kd
from text import text_start,text_help,text_Inversion,text_GreyScale,text_Sobel,text_Glass


#Start
# @dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    print("User:",message.from_user.full_name,"opened the bot; time:",message.date)
    await bot.send_message(message.from_user.id,text_start,reply_markup=main_kd)


#Help
# @dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
        print("User:",message.from_user.full_name,"executed command '/help'; time:",message.date)
        await bot.send_message(message.from_user.id,text_help)

#Information about filters
# @dp.message_handler(commands=['info'])
async def command_info(message: types.Message):
        print("User:",message.from_user.full_name,"executed command '/info'; time:",message.date)
        await bot.send_message(message.from_user.id,"Описание фильтров:")
        await bot.send_photo(message.from_user.id,photo=open('Images/Inversion.png', 'rb'),caption=text_Inversion)
        await bot.send_photo(message.from_user.id,photo=open('Images/Sobel.png', 'rb'),caption=text_Sobel)
        await bot.send_photo(message.from_user.id,photo=open('Images/GreyScale.png', 'rb'),caption=text_GreyScale)
        await bot.send_photo(message.from_user.id,photo=open('Images/Glass.png', 'rb'),caption=text_Glass)



def register_handlers_menu(dp:Dispatcher):
    dp.register_message_handler(command_start,commands=['start'],state='*')   
    dp.register_message_handler(command_help,commands=['help'])
    dp.register_message_handler(command_info,commands=['info'])
   