
from os import stat
from aiogram import types,Dispatcher
from create_bot import dp,bot
from keyboards import main_kd,filters_kd


#Start
# @dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    print("User:",message.from_user.full_name,"opened the bot; time:",message.date)
    await bot.send_message(message.from_user.id,"Вас приветствует бот ImProc-3000! Здесь вы можете загрузить ваши изображения и обработать их с помощью различных фильтров"
    ,reply_markup=main_kd)


#Help
# @dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
        print("User:",message.from_user.full_name,"executed command '/help'; time:",message.date)
        await bot.send_message(message.from_user.id,"Инструкция:")

#Information about filters
# @dp.message_handler(commands=['info'])
async def command_info(message: types.Message):
        print("User:",message.from_user.full_name,"executed command '/info'; time:",message.date)
        await bot.send_message(message.from_user.id,"Описание фильтров:")


        


def register_handlers_menu(dp:Dispatcher):
    dp.register_message_handler(command_start,commands=['start'],state='*')   
    dp.register_message_handler(command_help,commands=['help'])
    dp.register_message_handler(command_info,commands=['info'])
   