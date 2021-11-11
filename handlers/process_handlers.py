import io
from os import stat,remove
from aiogram import types,Dispatcher
from aiogram.dispatcher.filters import state
from aiogram.dispatcher.filters import Text
from create_bot import dp,bot
from keyboards import main_kd,filters_kd

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from text import text_start_processing

image_name=0


import ImageProc

class FSM(StatesGroup):
    photo=State()
    process=State()

#StartingFSM
async def start_processing(message: types.Message, state:FSMContext):
    print("User:",message.from_user.full_name,"executed command '/process'; time:",message.date)
    await FSM.photo.set()
    await bot.send_message(message.from_user.id,text_start_processing,reply_markup=filters_kd)

#Exit ti main menu
async def exit_to_menu(message: types.Message,state:FSMContext):
    print("User:",message.from_user.full_name,"executed command '/main_menu'; time:",message.date)
    await state.finish()
    await bot.send_message(message.from_user.id,"Выхожу в главное меню",reply_markup=main_kd)



#Loading photo
#@dp.message_handler(content_types=['photo'],state=FSM.photo)
async def load_image(message: types.Message,state:FSMContext):
    print("User:",message.from_user.full_name,"loaded a photo; time:",message.date)

    async with state.proxy() as data:
        data['document'] = message.document.file_id

    await FSM.process.set()

    await bot.send_message(message.from_user.id,"Картинка загружена\nПожалуйста, выберете фильтр:")


#Inversion
#@dp.message_handler(commands=['inversion'],state=FSM.process)
async def inversion(message: types.Message,state:FSMContext):
    print("User:",message.from_user.full_name,"executed command '/inversion'; time:",message.date)

    
    async with state.proxy() as data:
        file_id=await bot.get_file(data['document'])
    
    await bot.download_file(file_id.file_path,'Sources/'+str(message.from_user.id)+'.jpg')
    
    print("sending")
    image=ImageProc.Inversion(message.from_user.id)
    
    await bot.send_photo(message.from_user.id,image,caption="Инверсия")
   

#Sobel
#@dp.message_handler(commands=['sobel'],state=FSM.process)
async def sobel(message: types.Message,state:FSMContext):
    print("User:",message.from_user.full_name,"executed command '/sobel'; time:",message.date)
    async with state.proxy() as data:
        file_id=await bot.get_file(data['document'])

    await bot.download_file(file_id.file_path,'Sources/'+str(message.from_user.id)+'.jpg')
    
    print("sending")
    image=ImageProc.Sobel(message.from_user.id)
    
    await bot.send_photo(message.from_user.id,image,caption="Фильтр Собеля:")

#Grey Scale     
#@dp.message_handler(commands=['grey_scale'],state=FSM.process)
async def grey_scale(message: types.Message,state:FSMContext):
    print("User:",message.from_user.full_name,"executed command '/grey_scale'; time:",message.date)
    async with state.proxy() as data:
        file_id=await bot.get_file(data['document'])

    await bot.download_file(file_id.file_path,'Sources/'+str(message.from_user.id)+'.jpg')
    
    print("sending")
    image=ImageProc.GreyScale(message.from_user.id)
    
    await bot.send_photo(message.from_user.id,image,caption="Оттенки серого:")

#Glass   
#@dp.message_handler(commands=['glass'],state=FSM.process)
async def glass(message: types.Message,state:FSMContext):
    print("User:",message.from_user.full_name,"executed command '/glass'; time:",message.date)
    async with state.proxy() as data:
        file_id=await bot.get_file(data['document'])

    await bot.download_file(file_id.file_path,'Sources/'+str(message.from_user.id)+'.jpg')
    
    print("sending")
    image=ImageProc.Glass(message.from_user.id)
    
    await bot.send_photo(message.from_user.id,image,caption="Эффект стекла")



async def get_state(message: types.Message,state:FSMContext):
    print("User:",message.from_user.full_name,"executed command '/state'; time:",message.date)
    cur_state=await state.get_state()
    await bot.send_message(message.from_user.id,str(cur_state))

async def compressed_photo_sended(message: types.Message,state:FSMContext):
    await bot.send_message(message.from_user.id,"Пожалуйста, загрузите картинку, которую вы хотите обработать в виде файла.\nТогда она не будет подвержена сжатию")
        
def register_handlers_process(dp:Dispatcher):
    dp.register_message_handler(start_processing,commands=['process'],state=None)

    dp.register_message_handler(exit_to_menu,state=["*",None],commands='main_menu')
    dp.register_message_handler(exit_to_menu,Text(equals='main menu',ignore_case=True),state=["*",None])

    dp.register_message_handler(load_image,content_types=['document'],state=[FSM.photo,FSM.process])
    
    dp.register_message_handler(inversion,commands=['inversion'],state=FSM.process)    
    dp.register_message_handler(sobel,commands=['sobel'],state=FSM.process)
    dp.register_message_handler(grey_scale,commands=['grey_scale'],state=FSM.process)
    dp.register_message_handler(glass,commands=['glass'],state=FSM.process)
    dp.register_message_handler(get_state,commands=['state'],state='*')
    dp.register_message_handler(compressed_photo_sended,content_types=['photo'],state=[FSM.photo,FSM.process])