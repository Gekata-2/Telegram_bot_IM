from os import stat
from aiogram import types,Dispatcher
from aiogram.dispatcher.filters import state
from aiogram.dispatcher.filters import Text
from create_bot import dp,bot
from keyboards import main_kd,filters_kd

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

image_name=0


import ImageProc

class FSM(StatesGroup):
    photo=State()
    process=State()

#StartingFSM
async def start_processing(message: types.Message, state:FSMContext):
    print("User:",message.from_user.full_name,"executed command '/process'; time:",message.date)
    await FSM.photo.set()
    await bot.send_message(message.from_user.id,"""Для того чтобы а затем выберете интересующий вас фильтр
Загрузив картинку один раз вы можете применять к ней филтры несколько раз\nЧтобы загрузить другую картинку нажмите ещё раз /load_image
Чтобы вернуться в главное меню нажмите /main_menu """,reply_markup=filters_kd)

#Exit ti main menu
async def exit_to_menu(message: types.Message,state:FSMContext):
    current_state=await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await bot.send_message(message.from_user.id,"Exiting to main menu",reply_markup=main_kd)



#Loading photo
#@dp.message_handler(content_types=['photo'],state=FSM.photo)
async def load_image(message: types.Message,state:FSMContext):
    print("User:",message.from_user.full_name,"photo loaded; time:",message.date)

    async with state.proxy() as data:
        data['document'] = message.document.file_id

    await FSM.process.set()

    await bot.send_message(message.from_user.id,"Выбирите фильтр:")


#Inversion
#@dp.message_handler(commands=['inversion'],state=FSM.process)
async def inversion(message: types.Message,state:FSMContext):
    print("User:",message.from_user.full_name,"executed command '/inversion'; time:",message.date)

    await bot.send_message(message.from_user.id,"Inversion:")
    async with state.proxy() as data:
        file=await bot.get_file(data['document'])

    await bot.download_file(file.file_path,"image.jpg")
           
    global image_name
    image_name+=1
          
    await bot.send_photo(message.from_user.id,ImageProc.Inversion(str(image_name)+'.jpg'))
   

#Sobel
#@dp.message_handler(commands=['sobel'],state=FSM.process)
async def sobel(message: types.Message,state:FSMContext):
    print("User:",message.from_user.full_name,"executed command '/sobel'; time:",message.date)
    await bot.send_message(message.from_user.id,"Sobel:")
    async with state.proxy() as data:
        file=await bot.get_file(data['document'])

    await bot.download_file(file.file_path,"image.jpg")
           
    global image_name
    image_name+=1
          
    await bot.send_photo(message.from_user.id,ImageProc.Sobel(str(image_name)+'.jpg'))

#Grey Scale     
#@dp.message_handler(commands=['grey_scale'],state=FSM.process)
async def grey_scale(message: types.Message,state:FSMContext):
    print("User:",message.from_user.full_name,"executed command '/grey_scale'; time:",message.date)
    await bot.send_message(message.from_user.id,"Grey scale:")
    async with state.proxy() as data:
        file=await bot.get_file(data['document'])

    await bot.download_file(file.file_path,"image.jpg")
           
    global image_name
    image_name+=1
          
    await bot.send_photo(message.from_user.id,ImageProc.GreyScale(str(image_name)+'.jpg'))

#Glass   
#@dp.message_handler(commands=['glass'],state=FSM.process)
async def glass(message: types.Message,state:FSMContext):
    print("User:",message.from_user.full_name,"executed command '/glass'; time:",message.date)
    await bot.send_message(message.from_user.id,"Glass")
    async with state.proxy() as data:
        file=await bot.get_file(data['document'])

    await bot.download_file(file.file_path,"image.jpg")
           
    global image_name
    image_name+=1
          
    await bot.send_photo(message.from_user.id,ImageProc.Glass(str(image_name)+'.jpg'))



async def get_state(message: types.Message,state:FSMContext):
    print("User:",message.from_user.full_name,"executed command '/state'; time:",message.date)
    cur_state=await state.get_state()
    await bot.send_message(message.from_user.id,str(cur_state))

async def compressed_photo_sended(message: types.Message,state:FSMContext):
    await bot.send_message(message.from_user.id,"Пожалуйста, загрузите картинку, которую вы хотите обработать в виде файла.\nТогда она не будет подвержена сжатию")
        
def register_handlers_process(dp:Dispatcher):
    dp.register_message_handler(start_processing,commands=['process'],state=None)

    dp.register_message_handler(exit_to_menu,state="*",commands='main_menu')
    dp.register_message_handler(exit_to_menu,Text(equals='main menu',ignore_case=True),state="*")

    dp.register_message_handler(load_image,content_types=['document'],state=[FSM.photo,FSM.process])
    
    dp.register_message_handler(inversion,commands=['inversion'],state=FSM.process)    
    dp.register_message_handler(sobel,commands=['sobel'],state=FSM.process)
    dp.register_message_handler(grey_scale,commands=['grey_scale'],state=FSM.process)
    dp.register_message_handler(glass,commands=['glass'],state=FSM.process)
    dp.register_message_handler(get_state,commands=['state'],state='*')
    dp.register_message_handler(compressed_photo_sended,commands=['photo'],state=FSM.process)